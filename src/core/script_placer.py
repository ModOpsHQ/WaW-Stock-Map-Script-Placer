# /*===================================
#     Stock Imports
# ====================================*/

import logging
import os
from PySide6.QtCore import QTimer, Slot

# /*===================================
#     Configure Logging
# ====================================*/

logger = logging.getLogger(__name__)

from src.core.script_placer_worker import FileCopyWorker
from src.utils.message_box import display_message_box

# /*===================================
#     Main
# ====================================*/

class InputValidationAbort(Exception):
    """Custom exception to escape input validation warnings and hault the flow of execution"""
    pass

class ScriptPlacer:
    def __init__(self, mainWindow, currentWorkingDir, wawRootDir) -> None:
        self.mainWindow = mainWindow
        self.currentWorkingDir = currentWorkingDir
        self.wawRootDir = wawRootDir

        self.modffWarningOrErrorOccuredDuringBuild = False
        self.modffWarningOrErrorLogs = []

        from Resources.UI.ui_main_window import Ui_MainWindow
        self.ui: Ui_MainWindow = self.mainWindow.ui

        from Core.console import Console
        self.console = Console()
        self.console.ui.close_console_btn.hide()  # only show when an error
        self.console.ui.close_console_btn.clicked.connect(self.hideConsole)

        self.optionsWidgets = {
            'sp': {
                "ber1": self.ui.sp_ber1_cbox,
                "ber2": self.ui.sp_ber2_cbox,
                "ber3": self.ui.sp_ber3_cbox,
                "ber3b": self.ui.sp_ber3b_cbox,
                "mak": self.ui.sp_mak_cbox,
                "oki2": self.ui.sp_oki2_cbox,
                "oki3": self.ui.sp_oki3_cbox,
                "pby_fly": self.ui.sp_pby_fly_cbox,
                "pel1": self.ui.sp_pel1_cbox,
                "pel1a": self.ui.sp_pel1a_cbox,  # ff extractor has failed to extract the files
                "pel1b": self.ui.sp_pel1b_cbox,
                "pel2": self.ui.sp_pel2_cbox,
                "see1": self.ui.sp_see1_cbox,
                "see2": self.ui.sp_see2_cbox,
                "sniper": self.ui.sp_sniper_cbox
            },
            'mp': {
                "mp_airfield": self.ui.mp_airfield_cbox,
                "mp_asylum": self.ui.mp_asylum_cbox,
                "mp_bgate": self.ui.mp_bgate_cbox,
                "mp_castle": self.ui.mp_castle_cbox,
                "mp_courtyard": self.ui.mp_courtyard_cbox,
                "mp_docks": self.ui.mp_docks_cbox,
                "mp_dome": self.ui.mp_dome_cbox,
                "mp_downfall": self.ui.mp_downfall_cbox,
                "mp_drum": self.ui.mp_drum_cbox,
                "mp_hangar": self.ui.mp_hangar_cbox,
                "mp_kneedeep": self.ui.mp_kneedeep_cbox,
                "mp_kwai": self.ui.mp_kwai_cbox,
                "mp_makin": self.ui.mp_makin_cbox,
                "mp_makin_day": self.ui.mp_makin_day_cbox,
                "mp_nachtfeuer": self.ui.mp_nachtfeuer_cbox,
                "mp_outskirts": self.ui.mp_outskirts_cbox,
                "mp_roundhouse": self.ui.mp_roundhouse_cbox,
                "mp_seelow": self.ui.mp_seelow_cbox,
                "mp_shrine": self.ui.mp_shrine_cbox,
                "mp_stalingrad": self.ui.mp_stalingrad_cbox,
                "mp_suburban": self.ui.mp_suburban_cbox,
                "mp_subway": self.ui.mp_subway_cbox,
                "mp_vodka": self.ui.mp_vodka_cbox
            },
            'zm': {
                "nazi_zombie_prototype": self.ui.zm_prototype_cbox,
                "nazi_zombie_asylum": self.ui.zm_asylum_cbox,
                "nazi_zombie_sumpf": self.ui.zm_sumpf_cbox,
                "nazi_zombie_factory": self.ui.zm_factory_cbox
            }
        }

        self.ui.submit_btn.clicked.connect(self.createMod)

    def createMod(self):
        # ensure wawRootDir is valid
        if not os.path.exists(self.wawRootDir):
            msg = f"Error: The wawRootDir '{self.wawRootDir}' does not exist"
            logger.debug(msg)
            display_message_box(msg)
            return        
        
        try:
            modName, mapName, mode = self.verifyInputs()
        except InputValidationAbort as warning:
            # Explicitly stop execution if input validation fails
            self.updateStatusBar(str(warning))
            return
        except Exception as err:
            logger.error(err)
            display_message_box(f'Error: {err}')
            return
        
        # get the template files directory
        assetsRootDir = os.path.join(self.currentWorkingDir, 'ModOps HQ',  'Stock-Map Script-Placer')
        if not os.path.exists(assetsRootDir):
            os.makedirs(assetsRootDir)
        
        # join the template files root directory with the assets directory
        baseFilesDir = os.path.join(assetsRootDir, 'Stock Base Files', mode, mapName)
        if not os.path.exists(baseFilesDir):
            display_message_box(f"Error: The base files directory '{baseFilesDir}' does not exist")
            return

        # we've already previously checked that the modName doesn't exist, so we can safely create the mod dir
        modDir = os.path.join(self.wawRootDir, 'mods', modName)
        if not os.path.exists(modDir):
            os.makedirs(modDir)

        # temporarily disable the submit button
        self.ui.submit_btn.setEnabled(False)

        # in-case user didn't prev close the console (only possible if there was an error)
        self.modffWarningOrErrorOccuredDuringBuild = False
        self.modffWarningOrErrorLogs.clear()
        self.console.ui.console.clear()
        self.console.ui.close_console_btn.hide()

        self.initWorker(baseFilesDir, modDir, modName, mapName, mode)
    
    def verifyInputs(self):
        modName = self.ui.mod_name_input.text()
        if modName == "":
            raise InputValidationAbort('Warning, Please enter a mod name')

        if os.path.exists(os.path.join(self.wawRootDir, "mods", modName)):
            raise InputValidationAbort(f'Warning, {modName} already exists')

        if not self.isAnyCheckboxChecked():
            raise InputValidationAbort('Warning, Please select at least one map')

        if not self.isOnlyOneCheckboxChecked():
            raise InputValidationAbort('Warning, Please select only one map')

        # At this point, we know exactly one checkbox is selected
        mode = self.getSelectedCheckboxMode()
        mapName = self.getSelectedCheckboxMap()

        return modName, mapName, mode
    
    def isAnyCheckboxChecked(self) -> bool:
        # Iterate over all checkboxes in the nested dictionaries
        for category in self.optionsWidgets.values():
            for checkbox in category.values():
                if checkbox.isChecked():
                    return True
        return False
    
    def isOnlyOneCheckboxChecked(self) -> bool:
        # Counter for how many checkboxes are checked
        checked_count = 0

        # Iterate over all checkboxes in the nested dictionaries
        for category in self.optionsWidgets.values():
            for checkbox in category.values():
                if checkbox.isChecked():
                    checked_count += 1
                    if checked_count > 1:
                        return False  # More than one checkbox is checked

        # If exactly one checkbox is checked, return True
        return True
    
    def getSelectedCheckboxMode(self) -> str:
        # Iterate over all checkboxes to find the checked one
        for mode, category in self.optionsWidgets.items():
            for _, checkbox in category.items():
                if checkbox.isChecked():
                    return mode  # Return the mode of the checked checkbox

        # No need for a fallback since validation ensures exactly one is checked

    def getSelectedCheckboxMap(self) -> str:
        # Iterate over all checkboxes to find the checked one
        for category in self.optionsWidgets.values():
            for checkbox_name, checkbox in category.items():
                if checkbox.isChecked():
                    return checkbox_name  # Return the name of the checked checkbox

        # No need for a fallback since validation ensures exactly one is checked

    def initWorker(self, baseFilesDir, modDir, modName, mapName, mode):
        # get this check out of the way now to preven multiple builds
        self.createShortcut = self.ui.shortcut_cbox.isChecked()
        self.runExecutable = self.ui.run_map_cbox.isChecked()
        self.insertIngamePrintMsg = self.ui.insert_ingame_print_msg_cbox.isChecked()

        # Use shutil.copytree to copy the folder and its contents
        # Create and start the worker thread
        self.copy_worker = FileCopyWorker(
            wawRootDir=self.wawRootDir,
            src=baseFilesDir, dest=modDir,
            modName=modName, mapName=mapName, mode=mode,
            create_shortcut=self.createShortcut,
            insert_ingame_print_msg=self.insertIngamePrintMsg,
            build_mod=self.ui.build_mod_cbox.isChecked(),
            run_executable=self.runExecutable
        
        )
        # Connect signals and slots
        self.copy_worker.show_console.connect(self.console.show)
        self.copy_worker.update_status_bar.connect(self.updateStatusBar)
        self.copy_worker.send_display_message_box_message.connect(lambda message: display_message_box(message))
        self.copy_worker.finished.connect(self.onWorkerFinished)

        # mod.ff & iwd
        self.copy_worker.build_output_handle.connect(lambda message: self.console.ui.console.appendPlainText(message))
        # self.copy_worker.build_interrupted_handle.connect(self.buildInterruptedHandleSlot)  # this feature is not required for this app.
        
        # mod.ff
        self.copy_worker.build_output_warning_handle.connect(self.buildModFFWarningOutputHandleSlot)
        self.copy_worker.build_output_error_handle.connect(self.buildModFFErrorOutputHandleSlot)
        self.copy_worker.build_modff_success_handle.connect(lambda message: logger.debug(f'On build modff success: {message}'))  # 'All steps completed successfully'
        self.copy_worker.build_modff_failure_handle.connect(lambda message: logger.debug(f'On build modff failure: {message}'))
        
        # iwd
        self.copy_worker.build_iwd_success_handle.connect(lambda message: logger.debug(f'On build iwd success: {message}'))  # 'All steps completed successfully')
        self.copy_worker.build_iwd_failure_handle.connect(lambda message: logger.debug(f'On build iwd failure: {message}'))

        self.copy_worker.start()
        
    @Slot()
    def hideConsole(self) -> None:
        self.console.ui.console.clear()
        self.console.hide()
        self.modffWarningOrErrorOccuredDuringBuild = False
        self.modffWarningOrErrorLogs.clear()
    
    @Slot(str, int)
    def updateStatusBar(self, message, delay=3000) -> None:
        self.ui.statusBar.showMessage(message, delay)
    
    # mod.ff
    @Slot(str)
    def buildModFFWarningOutputHandleSlot(self, message: str) -> None:
        logger.debug('WARNING occured during modff build')
        self.modffWarningOrErrorOccuredDuringBuild = True
        self.modffWarningOrErrorLogs.append(message)
    
    @Slot(str)
    def buildModFFErrorOutputHandleSlot(self, message: str) -> None:
        logger.debug('ERROR occured during modff build')
        self.modffWarningOrErrorOccuredDuringBuild = True
        self.modffWarningOrErrorLogs.append(message)        

    @Slot(bool, str)
    def onWorkerFinished(self, result, message) -> None:
        delay = 5000

        if result:
            self.updateStatusBar(message, delay)
            
            if self.modffWarningOrErrorOccuredDuringBuild:
                self.console.ui.console.appendPlainText('\n/************** Here is the list of warnings/errors. *****************/')
                self.console.ui.console.appendPlainText('\n'.join(self.modffWarningOrErrorLogs))
                self.console.ui.close_console_btn.show()
            else:
                self.console.ui.console.clear()
                self.console.hide()

            # scroll to the bottom, sometimes it doesnt do it fully automatically
            self.console.ui.console.verticalScrollBar().setValue(self.console.ui.console.verticalScrollBar().maximum() + 100)
        else:
            display_message_box(message)
        
        # if failure, the display_message_box function is blocking, so have the mod creation delay start after the message_box has been closed.
        QTimer.singleShot(delay, lambda: self.ui.submit_btn.setEnabled(True))

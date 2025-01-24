# /*===================================
#     Stock Imports
# ====================================*/

import logging
import os
import shutil
import subprocess
from PySide6.QtCore import QThread, Signal

# /*===================================
#     Configure Logging
# ====================================*/

logger = logging.getLogger(__name__)

# /*===================================
#     Main
# ====================================*/

import src.components.build_mod_ff as build_mod_ff
import src.components.build_iwd as build_iwd
import src.components.insert_gsc_code as insert_gsc_code
from src.utils.is_executable import is_executable

class FileCopyWorker(QThread):
    # signals
    show_console = Signal(bool)
    update_status_bar = Signal(str, int)
    send_display_message_box_message = Signal(str)
    finished = Signal(bool, str)

    # mod.ff & iwd
    build_output_handle = Signal(str)
    build_interrupted_handle = Signal(str)

    # mod.ff
    build_output_warning_handle = Signal(str)  # doesnt have modff in the name cause theres no iwd equivalent
    build_output_error_handle = Signal(str)  # doesnt have modff in the name cause theres no iwd equivalent
    build_modff_success_handle = Signal(str)
    build_modff_failure_handle = Signal(str)

    # iwd
    build_iwd_success_handle = Signal(str)
    build_iwd_failure_handle = Signal(str)

    def __init__(self, wawRootDir, src, dest, modName, mapName, mode, create_shortcut=False, insert_ingame_print_msg=False, build_mod=False, run_executable=False):
        super().__init__()
        self.wawRootDir = wawRootDir
        self.src = src
        self.dest = dest
        self.modName = modName
        self.mapName = mapName
        self.mode = mode
        self.create_shortcut = create_shortcut
        self.build_mod = build_mod
        self.run_executable = run_executable
        self.insert_ingame_print_msg = insert_ingame_print_msg

        self.exeName = 'CoDWaW' if self.mode != 'mp' else 'CoDWaWmp'

    def run(self):
        try:
            self.copyFiles()
        
            if self.create_shortcut:
                self.createShortcut(self.wawRootDir)
            
            if self.insert_ingame_print_msg:
                self.insertIngamePrintMsg()

            if self.build_mod:
                self.show_console.emit(True)
                self.buildMod()
        
            if self.run_executable:
                self.runExecutable()

            self.exitWorker(True, f"Successfully created '{self.modName}' for '{self.mapName}' on '{self.mode}'")
        except subprocess.CalledProcessError as err:
            self.exitWorker(False, f"Error: {err}")
        except Exception as err:
            self.exitWorker(False, f"Error: {err}")
    
    def exitWorker(self, qbool: bool, msg: str) -> None:
        logger.debug(msg)
        self.finished.emit(qbool, msg)

    def copyFiles(self):
        shutil.copytree(self.src, self.dest, dirs_exist_ok=True)

    def createShortcut(self, wawRootDir):
        wawArgs = rf'+set fs_game mods/{self.modName} +devmap {self.mapName} +set r_fullscreen 0'
        wawPath = rf'"{wawRootDir}\{self.exeName}.exe"'  # root + exe requires to be wrapped in double quotes

        newShortcutPath = os.path.expanduser(rf'~\Desktop\{self.modName}.lnk')  # store on users desktop
        iconPath = rf'{wawRootDir}\{self.exeName}.ico'
        if not os.path.exists(iconPath):
            iconPath = None
        startInPath = wawRootDir  # "Start In" path (working directory)

        PyUtility.createShortcut(
            target=wawPath,  # this is the "Target" Path (exe > properties > shorcut tab > target path field)
            shortcut_dest=newShortcutPath,  # store shortcut on the user's desktop
            icon_path=iconPath,  # Set icon
            args=wawArgs,  # set the target path args
            start_in=startInPath  # set the "Start In" path
        )

    def buildMod(self) -> None:
        build_mod_ff.build(
            ### These are all required args and dont need to be changed ###
            modDir=os.path.join(self.wawRootDir, 'mods', self.modName),
            zoneSourceDir=os.path.join(self.wawRootDir, 'zone_source'),
            modName=self.modName,
            binDir=os.path.join(self.wawRootDir, 'bin'),
            zoneEnglishDir=os.path.join(self.wawRootDir, 'zone', 'english'),
            activisionModDir=os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Activision', 'CoDWaW', 'mods', self.modName),  # '~' = home dir: 'C:\Users\Phil-\'

            ### These are all optional args and can be changed ###
            buildOutputHandle=self.buildOutputHandleSlot,  # uses print by default
            buildWarningOutputHandle=self.build_output_warning_handle.emit,  # looks for a specific output marker: 'WARNING:'
            buildErrorOutputHandle=self.build_output_error_handle.emit,  # looks for a specific output marker: 'ERROR:'
            buildSuccessHandle=self.build_modff_success_handle.emit,  # 'All steps completed successfully'
            buildFailureHandle=self.build_modff_failure_handle.emit,  # f'Step {step.__name__} failed: {error}'
            buildInterruptedHandle=self.build_interrupted_handle.emit,  # 'Process was interrupted by the user'
            addSpaceBetweenSteps=True,
            msgGroupSize=10
        )

        self.build_output_handle.emit('\n')  # to separate the output

        build_iwd.build(
            ### These are all required args and dont need to be changed ###
            modName=self.modName,
            modDir=os.path.join(self.wawRootDir, 'mods', self.modName),
            activisionModDir=os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Activision', 'CoDWaW', 'mods', self.modName),  # '~' = home dir

            ### These are all optional args and can be changed ###
            foldersToIgnore=[
                # 'sound',
            ],
            filesToIgnore=[],
            extensionsToIgnore=[
                '.ff',
                '.iwd',
                '.log',
                '.txt',
                '.files',
            ],
            ### These are all optional args and can be changed ###
            buildOutputHandle=self.buildOutputHandleSlot,  # uses print by default
            buildSuccessHandle=self.build_iwd_success_handle.emit,  # 'All steps completed successfully'
            buildFailureHandle=self.build_iwd_failure_handle.emit,  # f'Step {step.__name__} failed: {error}'
            buildInterruptedHandle=self.build_interrupted_handle.emit,  # 'Process was interrupted by the user'
            addSpaceBetweenSteps=True,
            msgGroupSize=10
        )
    
        self.build_output_handle.emit('\n')  # to separate old output from new

    # mod.ff & iwd
    def buildOutputHandleSlot(self, message: str) -> None:
        self.build_output_handle.emit(message)

    def runExecutable(self):
        dir = self.wawRootDir if not is_executable() else os.getcwd()
        _, message = PyUtility.runExecutable(
            running_dir=dir,
            exe_path=os.path.join(dir, f'{self.exeName}.exe'),
            exe_args=rf'+set fs_game mods/{self.modName} +devmap {self.mapName} +set r_fullscreen 0'
        )
        logger.debug(message)

    def insertIngamePrintMsg(self):
        message = f'Mod: {self.modName} was built successfully!'

        match self.mode:
            case 'sp':
                line_identifier = r'maps\_load::main('
                file_path = os.path.join(self.dest, 'maps', f'{self.mapName}.gsc')
                append_str = f"""\npost() {{  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1
    wait 10;
    iPrintLn( "{message}" );
}}"""
            case 'mp':
                line_identifier = r'maps\mp\_load::main('
                file_path = os.path.join(self.dest, 'maps', 'mp', f'{self.mapName}.gsc')
                append_str = f"""\npost() {{  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1
    wait 15;
    iPrintLn( "{message}" );
}}"""
            case 'zm':
                line_identifier = r'maps\_zombiemode::main('
                file_path = os.path.join(self.dest, 'maps', f'{self.mapName}.gsc')
                append_str = f"""\npost() {{  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1
    flag_wait("all_players_connected");
    wait 1;
    iPrintLn( "{message}" );
}}"""

            case _:
                raise Exception(f'Unknown mode: {self.mode}')

        insert_gsc_code.insertMarkerToConfirmTheBuildsValidity(
            file_path=file_path,
            line_identifier=line_identifier,
            insert_str='\n	thread post();  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1',
            append_str=append_str
        )

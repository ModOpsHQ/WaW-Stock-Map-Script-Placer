""" NOTE
    (1):
        When testing, you will need to replace the below 'wawRootDir' with your actual WAW root directory
        as well as the 'modName' with the actual name of your mod.

    (2):
        The default stock mod launcher behaviour is to copy modName.iwd to appdata/mods folder if it is not present there during the mod.ff stage.
        So this module does take care of that, but for the actual building of the .iwd, check out the 'build_iwd.py' module.

    (3):
        During the copy mod.csv from mod folder to zone_source folder stage, if said mod.csv file does not exist, it will be created.

    (4):
        When using this in a GUI application, you will need to grab the text from your mod.csv widget section and paste it into the mod.csv file before copying it from mods > zone_source.
        I've added the logic to copy content from mod.csv in mod folder to zone_source folder. So all you need to do for a GUI-based application is copy text from mod.csv widget-section to mod.csv file in mod folder then this module can take care of the rest.      
"""

# /*===================================
#     Stock Imports
# ====================================*/

import csv
import logging
import os
import shutil
import subprocess
from typing import Callable, Optional

# /*===================================
#     Configure Logging
# ====================================*/

logger = logging.getLogger(__name__)

# /*===================================
#     Main
# ====================================*/

stepFailure = False
processInterrupted = False

def build(
        modDir: str, zoneSourceDir: str, modName: str, binDir: str, zoneEnglishDir: str, activisionModDir: str,
        buildOutputHandle=print,
        buildWarningOutputHandle: Optional[Callable]=None, buildErrorOutputHandle: Optional[Callable]=None,
        buildSuccessHandle: Optional[Callable]=None, buildFailureHandle: Optional[Callable]=None,
        buildInterruptedHandle: Optional[Callable]=None,
        addSpaceBetweenSteps=False,
        msgGroupSize: int=1
    ) -> None:
    
    steps = [
        lambda arg1=modDir, arg2=zoneSourceDir, arg3=buildOutputHandle: copyModCsvFromModToZoneSource(arg1, arg2, arg3),
        lambda arg1=modName, arg2=binDir, arg3=buildOutputHandle, arg4=buildWarningOutputHandle, arg5=buildErrorOutputHandle, arg6=msgGroupSize: buildModFf(arg1, arg2, arg3, arg4, arg5, arg6),
        lambda arg1=zoneEnglishDir, arg2=modDir, arg3=buildOutputHandle: moveModFfFromZoneEnglishToMod(arg1, arg2, arg3),
        lambda arg1=activisionModDir, arg2=modDir, arg3=buildOutputHandle: copyModFfFromModToActivisionMod(arg1, arg2, arg3),
        lambda arg1=activisionModDir, arg2=modDir, arg3=modName, arg4=buildOutputHandle: copyIwdFromModToActivisionMod(arg1, arg2, arg3, arg4),
    ]

    # lambda's are anonymous functions, so we need to assign the function names manually
    # when not using lambda, 'step.__name__' would print the actual function name.
    steps[0].__name__ = 'copy_mod_csv_step'
    steps[1].__name__ = 'build_mod_ff_step'
    steps[2].__name__ = 'move_mod_ff_step'
    steps[3].__name__ = 'copy_mod_ff_step'
    steps[4].__name__ = 'copy_iwd_step'

    global stepFailure

    # import time

    for step in steps:
        if stepFailure:
            break
        if processInterrupted:
            break
        try:
            # start_time = time.time()  # Record the start time
            step()                    # Call the step function
            # elapsed_time = time.time() - start_time  # Calculate elapsed time
            # logger.debug(f"[modff]: Time taken for step {i}: {elapsed_time:.4f} seconds")

            if addSpaceBetweenSteps:
                buildOutputHandle('\n'.strip())  # it adds 2 newlines w/o .strip()
        except Exception as error:
            stepFailure = True
            if buildFailureHandle:
                buildFailureHandle(f'Step {step.__name__} failed: {error}')
    
    if processInterrupted:
        if buildInterruptedHandle:
            buildInterruptedHandle('Process was interrupted by the user')
        return

    if not stepFailure:
        buildOutputHandle('Everything is Ok')
        if buildSuccessHandle:
            buildSuccessHandle('All steps completed successfully')

def copyModCsvFromModToZoneSource(modDir: str, zoneSourceDir: str, buildOutputHandle: Callable) -> None:
    mod_csv_path = os.path.join(modDir, 'mod.csv')

    # Check if the file exists (this would usually be handled by the mod launcher)
    if not os.path.exists(mod_csv_path):
        with open(mod_csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            # Write your message in a separate row or as a valid CSV row
            writer.writerow(['// auto-generated during csv creation    // ModOps HQ - Build-Tools v1.1.2'])  # Comment-like message
    
    zone_source_path = os.path.join(zoneSourceDir, 'mod.csv')
    
    shutil.copy2(mod_csv_path, zone_source_path)

    buildOutputHandle(f'Copying  {mod_csv_path}')
    buildOutputHandle(f'     to  {zone_source_path}')

def buildModFf(
    modName: str,
    binDir: str,
    buildOutputHandle: Callable,
    buildWarningOutputHandle: Optional[Callable],
    buildErrorOutputHandle: Optional[Callable],
    msgGroupSize: int
) -> None:
    args = ['linker_pc', '-nopause', '-language', 'english', '-moddir', modName, 'mod']

    # Use Popen to run the linker asynchronously
    process = subprocess.Popen(
        args,
        cwd=binDir,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True  # Enable text mode for easier string handling
    )

    # Buffer for messages
    message_buffer = []

    # Read stdout and stderr in real time
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            output = output.strip()
            message_buffer.append(output)  # Add the output to the buffer

            # Check if the buffer has reached the specified group size
            if len(message_buffer) >= msgGroupSize:
                # Join messages and send them
                grouped_messages = "\n".join(message_buffer)
                buildOutputHandle(grouped_messages)
                message_buffer.clear()  # Clear the buffer after sending

            # Handle warnings and errors
            if output.startswith('WARNING:'):
                if buildWarningOutputHandle:
                    buildWarningOutputHandle(output)
            elif output.startswith('ERROR:'):
                if buildErrorOutputHandle:
                    buildErrorOutputHandle(output)

        if processInterrupted:  # user interrupted
            process.kill()
            return

    # After the process finishes, flush any remaining messages in the buffer
    if message_buffer:
        grouped_messages = "\n".join(message_buffer)
        buildOutputHandle(grouped_messages)

    # Capture the stderr output after the process finishes
    stderr = process.stderr.read()
    if stderr:
        buildOutputHandle(stderr.strip())

def moveModFfFromZoneEnglishToMod(zoneEnglishDir: str, modDir: str, buildOutputHandle: Callable) -> None:
    modFfSource = os.path.join(zoneEnglishDir, 'mod.ff')
    modFfDest = os.path.join(modDir, 'mod.ff')

    shutil.move(modFfSource, modFfDest)

    buildOutputHandle(f'Moving  {modFfSource}')
    buildOutputHandle(f'    to  {modFfDest}')

def copyModFfFromModToActivisionMod(activisionModDir: str, modDir: str, buildOutputHandle: Callable) -> None:
    if not os.path.exists(activisionModDir):
        os.makedirs(activisionModDir)

    modFfSource = os.path.join(modDir, 'mod.ff')
    modFfDest = os.path.join(activisionModDir, 'mod.ff')

    shutil.copy2(modFfSource, modFfDest)

    buildOutputHandle(f'Copying  {modFfSource}')
    buildOutputHandle(f'     to  {modFfDest}')

def copyIwdFromModToActivisionMod(activisionModDir: str, modDir: str, modName: str, buildOutputHandle: Callable) -> None:
    # Just a nice touch that the stock launcher has where it ensures the modName.iwd is present in appdata/mods folder during the mod.ff stage.
    
    if not os.path.exists(activisionModDir):
        os.makedirs(activisionModDir)

    modIwdSource = os.path.join(modDir, f'{modName}.iwd')
    modIwdDest = os.path.join(activisionModDir, f'{modName}.iwd')
    
    # step 1: check if present in root/mods
    if os.path.exists(modIwdSource):
        # print('iwd present in root/mods')

        # step 2: check if not present in appdata/mods
        if not os.path.exists(modIwdDest):
            # print('iwd not in appdata/mods')

            shutil.copy2(modIwdSource, modIwdDest)

            buildOutputHandle(f'Copying  {modIwdSource}')
            buildOutputHandle(f'     to  {modIwdDest}')
        else:
            buildOutputHandle(f'Skipping copying  {modIwdSource}')
            buildOutputHandle(f'              to  {modIwdDest}')
            buildOutputHandle('          Reason  iwd already present')
    else:
        buildOutputHandle(f'Skipping copying  {modIwdSource}')
        buildOutputHandle(f'              to  {modIwdDest}')
        buildOutputHandle('          Reason  iwd not present')

def interruptProcessHandle() -> None:
    global processInterrupted
    processInterrupted = True

# Example usage
if __name__ == '__main__':
    # change these 2 as needed
    # NOTE: Be careful with variables that are in global scope like the below 2.
    #       I changed their styling from the args styling so functions couldn't access them unless passed as args.
    mod_name = 'zm_test1'
    waw_root_dir = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War'

    # Feel free to copy/paste these functions into your own script.
    def buildModFFOutputHandleSlot(message: str) -> None:
        print(f'Captured output: {message}')
    
    def buildModFFWarningOutputHandleSlot(message: str) -> None:
        print(f'Captured warning from output: {message}')
    
    def buildModFFErrorOutputHandleSlot(message: str) -> None:
        print(f'Captured error from output: {message}')
    
    def buildModFFSuccessHandleSlot(message: str) -> None:
        print(f'On program success: {message}')

    def buildModFFFailureHandleSlot(message: str) -> None:
        print(f'On program failure: {message}')
    
    def buildModFFInterruptedHandleSlot(message: str) -> None:
        print(f'On process interrupted: {message}')

    # Imitates user interruption (just uncomment, adjust the delay and its good to go!).
    # import threading, time
    # threading.Thread(target=lambda: (time.sleep(0.1), interruptProcessHandle())).start()

    print()  # to separate from vs output
    build(
        ### These are all required args and dont need to be changed ###
        modDir=os.path.join(waw_root_dir, 'mods', mod_name),
        zoneSourceDir=os.path.join(waw_root_dir, 'zone_source'),
        modName=mod_name,
        binDir=os.path.join(waw_root_dir, 'bin'),
        zoneEnglishDir=os.path.join(waw_root_dir, 'zone', 'english'),
        activisionModDir=os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Activision', 'CoDWaW', 'mods', mod_name),  # '~' = home dir: 'C:\Users\Phil-\'

        ### These are all optional args and can be changed ###
        # buildOutputHandle=buildModFFOutputHandleSlot,  # uses print by default
        # buildWarningOutputHandle=buildModFFWarningOutputHandleSlot,  # looks for a specific output marker: 'WARNING:'
        # buildErrorOutputHandle=buildModFFErrorOutputHandleSlot,  # looks for a specific output marker: 'ERROR:'
        buildSuccessHandle=buildModFFSuccessHandleSlot,
        buildFailureHandle=buildModFFFailureHandleSlot,
        buildInterruptedHandle=buildModFFInterruptedHandleSlot,
        addSpaceBetweenSteps=True,
        # msgGroupSize=10
    )
    print()  # to separate from vs output

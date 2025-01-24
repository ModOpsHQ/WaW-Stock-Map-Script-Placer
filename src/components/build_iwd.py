""" NOTE
    (1):
        When testing, you will need to replace the below 'wawRootDir' with your actual WAW root directory
        as well as the 'modName' with the actual name of your mod.

    (2):
        The default stock mod launcher behaviour is to copy mod.ff to appdata/mods folder if it is not present there during the iwd stage.
        So this module does take care of that, but for the actual building of the mod.ff, check out the 'build_mod_ff.py' module.
"""

# /*===================================
#     Stock Imports
# ====================================*/

import logging
import os
import platform
import shutil
import zipfile
from datetime import datetime
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
        modName: str, modDir: str, activisionModDir: str,
        foldersToIgnore: list=[], filesToIgnore: list=[], extensionsToIgnore: list=[],
        buildOutputHandle: Callable=print,
        buildSuccessHandle: Optional[Callable]=None, buildFailureHandle: Optional[Callable]=None,
        buildInterruptedHandle: Optional[Callable]=None,
        addSpaceBetweenSteps=False, msgGroupSize: int=1
    ) -> None:

    buildOutputHandle(f'Python zipfile (P) {platform.python_version()}')
    buildOutputHandle(f'Copyright (c) 2001-{datetime.now().year} Python Software Foundation')
    buildOutputHandle('Scanning')
    x = '\n' if addSpaceBetweenSteps else ''  # if newline, add above and below
    buildOutputHandle(f'{x}Creating archive {os.path.join(modDir, f'{modName}.iwd')}{x}')

    steps = [
        lambda arg1=modDir, arg2=modName, arg3=foldersToIgnore, arg4=filesToIgnore, arg5=extensionsToIgnore, arg6=buildOutputHandle, arg7=msgGroupSize: buildIwd(arg1, arg2, arg3, arg4, arg5, arg6, arg7),
        lambda arg1=modName, arg2=modDir, arg3=activisionModDir, arg4=buildOutputHandle: copyModIwdFromModToActivisionMod(arg1, arg2, arg3, arg4),
        lambda arg1=activisionModDir, arg2=modDir, arg3=buildOutputHandle: copyModFfFromModToActivisionMod(arg1, arg2, arg3),
    ]

    # lambda's are anonymous functions, so we need to assign the function names manually
    # when not using lambda, the below '{step.__name__}' would work perfectly fine.
    steps[0].__name__ = 'build_iwd_step'
    steps[1].__name__ = 'copy_mod_iwd_step'
    steps[2].__name__ = 'copy_mod_ff_step'

    global stepFailure

    # import time

    for i, step in enumerate(steps):
        if stepFailure:
            break
        if processInterrupted:
            break
        try:
            # start_time = time.time()  # Record the start time
            step()                    # Call the step function
            # elapsed_time = time.time() - start_time  # Calculate elapsed time
            # logger.debug(f"[iwd]: Time taken for step {i}: {elapsed_time:.4f} seconds")

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

def buildIwd(
        modDir: str, modName: str,
        foldersToIgnore: list, filesToIgnore: list, extensionsToIgnore: list,
        buildOutputHandle: Callable, msgGroupSize: int
    ) -> None:

    array = []

    itemsToPkgIntoIwd = grabModStructure(
        rootDir=modDir,
        foldersToIgnore=foldersToIgnore,
        filesToIgnore=filesToIgnore,
        extensionsToIgnore=extensionsToIgnore
    )

    iterateFiles(data=itemsToPkgIntoIwd, action=lambda x: array.append(x), buildOutputHandle=buildOutputHandle)

    iwdDest = os.path.join(modDir, f'{modName}.iwd')

    # Delete old iwd if it exists
    if os.path.exists(iwdDest):
        os.remove(iwdDest)

    array = sorted(array)  # Sort in ascending order

    # Grouping messages for appending to console in blocks
    message_buffer = []

    for item in array:
        # Prepare the message for the current file being processed
        message_buffer.append(f'Compressing {item}')

        # Check if the buffer has reached the specified group size
        if len(message_buffer) >= msgGroupSize:
            # Join messages and send them
            grouped_messages = "\n".join(message_buffer)
            buildOutputHandle(grouped_messages)
            message_buffer.clear()  # Clear the buffer after sending

        # Add the file (item) to the zip archive
        with zipfile.ZipFile(iwdDest, 'a', zipfile.ZIP_DEFLATED) as zipf:
            file_to_add = os.path.join(modDir, item).replace('\\', '/')
            file_in_iwd = item

            # Add the file to the zip archive
            zipf.write(file_to_add, file_in_iwd)

        if processInterrupted:
            break

    # After the loop, flush any remaining messages in the buffer
    if message_buffer:
        grouped_messages = "\n".join(message_buffer)
        buildOutputHandle(grouped_messages)

# Utilized by: buildIwd()
def grabModStructure(rootDir: str=os.getcwd(), foldersToIgnore: list=[], filesToIgnore: list=[], extensionsToIgnore: list=[]) -> dict:
    structure = {}
    for item in os.listdir(rootDir):
        item_path = os.path.join(rootDir, item)
        if os.path.isdir(item_path):
            if any(folder in item for folder in foldersToIgnore):
                continue
            # Recursively build the folder structure
            structure[item] = grabModStructure(item_path, foldersToIgnore, filesToIgnore, extensionsToIgnore)
        else:
            # Check for file names and extensions to ignore
            if any(fileName in item for fileName in filesToIgnore) or any(item.endswith(ext) for ext in extensionsToIgnore):
                continue
            # Store the file in the dictionary
            structure[item] = None
    return structure

# Utilized by: buildIwd()
def iterateFiles(data: dict, action: Callable=None, buildOutputHandle=print, parent: str='') -> None:
    for key, value in data.items():
        current_path = f'{parent}/{key}' if parent else key  # Join parent with current folder/file
        if isinstance(value, dict):  # If value is a dictionary, recurse
            iterateFiles(data=value, action=action, buildOutputHandle=buildOutputHandle, parent=current_path)
        else:  # If it's a file (None in this case), print the path
            if action:
                action(current_path)

def copyModIwdFromModToActivisionMod(modName: str, modDir: str, activisionModDir: str, buildOutputHandle=print) -> None:
    modIwdSource = os.path.join(modDir, f'{modName}.iwd')
    modIwdDest = os.path.join(activisionModDir, f'{modName}.iwd')

    if not os.path.exists(activisionModDir):
        os.makedirs(activisionModDir)

    shutil.copy2(modIwdSource, modIwdDest)

    buildOutputHandle(f'Copying  {modIwdSource}')
    buildOutputHandle(f'     to  {modIwdDest}')

def copyModFfFromModToActivisionMod(activisionModDir: str, modDir: str, buildOutputHandle=print) -> None:
    # Just a nice touch that the stock launcher has where it ensures the mod.ff is present in appdata/mods folder during the iwd stage.
    modFfSource = os.path.join(modDir, 'mod.ff')
    modFfDest = os.path.join(activisionModDir, 'mod.ff')

    if not os.path.exists(activisionModDir):
        os.makedirs(activisionModDir)

    # step 1: check if present in root/mods
    if os.path.exists(modFfSource):
        # print('mod.ff present in root/mods')

        # step 2: check if not present in appdata/mods
        if not os.path.exists(modFfDest):
            # print('mod.ff not in appdata/mods')

            shutil.copy2(modFfSource, modFfDest)

            buildOutputHandle(f'Copying  {modFfSource}')
            buildOutputHandle(f'     to  {modFfDest}')
        else:
            buildOutputHandle(f'Skipping copying  {modFfSource}')
            buildOutputHandle(f'              to  {modFfDest}')
            buildOutputHandle('          Reason  mod.ff already present')
    else:
        buildOutputHandle(f'Skipping copying  {modFfSource}')
        buildOutputHandle(f'              to  {modFfDest}')
        buildOutputHandle('          Reason  mod.ff not present')

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
    def buildIWDOutputHandleSlot(message: str) -> None:
        print(f'Captured output: {message}')
    
    def buildIWDSuccessHandleSlot(message: str) -> None:
        print(f'On program success: {message}')

    def buildIWDFailureHandleSlot(message: str) -> None:
        print(f'On program failure: {message}')
    
    def buildIWDInterruptedHandleSlot(message: str) -> None:
        print(f'On process interrupted: {message}')
    
    # Imitates user interruption (just uncomment, adjust the delay and its good to go!).
    # import threading, time
    # threading.Thread(target=lambda: (time.sleep(0.1), interruptProcessHandle())).start()

    print()  # to separate from vs output
    build(
        ### These are all required args and dont need to be changed ###
        modName=mod_name,
        modDir=os.path.join(waw_root_dir, 'mods', mod_name),
        activisionModDir=os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Activision', 'CoDWaW', 'mods', mod_name),  # '~' = home dir

        ### These are all optional args and can be changed ###
        foldersToIgnore=[
            'sound',
        ],
        filesToIgnore=[
            # examples
            # 'how-to-notes.md',
            # 'screen-grab-of-map.png',
        ],
        extensionsToIgnore=[
            '.ff',
            '.iwd',
            '.log',
            '.txt',
            '.files',
        ],
        ### These are all optional args and can be changed ###
        # buildOutputHandle=buildIWDOutputHandleSlot,  # uses print by default
        buildSuccessHandle=buildIWDSuccessHandleSlot,
        buildFailureHandle=buildIWDFailureHandleSlot,
        buildInterruptedHandle=buildIWDInterruptedHandleSlot,
        addSpaceBetweenSteps=True,
        # msgGroupSize=10
    )
    print()  # to separate from vs output

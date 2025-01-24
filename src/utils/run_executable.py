# /*===================================
#     Stock Imports
# ====================================*/

import os
import subprocess
from typing import Union

# /*===================================
#     Main
# ====================================*/

def run_executable(running_dir: str, exe_path: str, exe_args: str) -> Union[bool, str]:
    """
    Runs the given executable with no arguments.
    exe_path: Path to the executable file
    """
    os.chdir(running_dir)  # required

    try:
        subprocess.Popen(
            [exe_path, exe_args],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        return True, f"Successfully ran {exe_path}"
    except subprocess.CalledProcessError as e:
        return False, f"Error occurred while running {exe_path}: {e}"
    except FileNotFoundError:
        return False, f"Executable not found: {exe_path}"
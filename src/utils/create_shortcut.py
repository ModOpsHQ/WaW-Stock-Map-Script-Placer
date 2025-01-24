# /*===================================
#     Stock Imports
# ====================================*/

from win32com.client import Dispatch

# /*===================================
#     Main
# ====================================*/

def create_shortcut(target: str, shortcut_dest: str, icon_path: str = None, args: str = None, start_in: str = None) -> None:
    """Create a shortcut to a target file with optional arguments and start-in path."""
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_dest)
    shortcut.TargetPath = target
    if args:
        shortcut.Arguments = args
    if icon_path:
        shortcut.IconLocation = icon_path
    if start_in:
        shortcut.WorkingDirectory = start_in  # Set the "Start In" directory
    shortcut.save()
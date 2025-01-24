# /*===================================
#     Stock Imports
# ====================================*/

import logging

# /*===================================
#     Configure Logging
# ====================================*/

logger = logging.getLogger(__name__)

# /*===================================
#     Main
# ====================================*/

def insertMarkerToConfirmTheBuildsValidity(file_path, line_identifier, insert_str, append_str):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Flag to check if the identifier is found
        identifier_found = False

        # Open the file in write mode
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line)
                
                # Check if the current line contains the line identifier
                if line_identifier in line and not identifier_found:
                    file.write(insert_str + '\n')
                    identifier_found = True
            
            # After writing all lines, append the append_str to the end of the file
            file.write('\n' + append_str + '\n')
        
        logger.debug(f"File '{file_path}' modified successfully.")

    except Exception as e:
        logger.exception(f'An error occurred: {e}')

# Usage example:
if __name__ == '__main__':
    import os

    mode = 'zm'
    modName = 'zm_test1'
    mapName = 'nazi_zombie_prototype'
    dest = rf'D:\SteamLibrary\steamapps\common\Call of Duty World at War\mods\{modName}'

    message = f'Mod: {modName} was built successfully!'
    
    match mode:
        case 'sp':
            line_identifier = r'maps\_load::main('
            file_path = os.path.join(dest, 'maps', f'{mapName}.gsc')
            append_str = f"""\npost() {{  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1
wait 10;
iPrintLn( "{message}" );
}}"""
        case 'mp':
            line_identifier = r'maps\mp\_load::main('
            file_path = os.path.join(dest, 'maps', 'mp', f'{mapName}.gsc')
            append_str = f"""\npost() {{  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1
wait 15;
iPrintLn( "{message}" );
}}"""
        case 'zm':
            line_identifier = r'maps\_zombiemode::main('
            file_path = os.path.join(dest, 'maps', f'{mapName}.gsc')
            append_str = f"""\npost() {{  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1
flag_wait("all_players_connected");
wait 1;
iPrintLn( "{message}" );
}}"""

        case _:
            raise Exception(f'Unknown mode: {self.mode}')

    import os
    insertMarkerToConfirmTheBuildsValidity(
        file_path=file_path,
        line_identifier=line_identifier,
        insert_str='\n	thread post();  // ModOps HQ (Price) - WaW-Stock-Map-Script-Placer v1.1.1',
        append_str=append_str
    )
import os
import re

def replace_priority(file_path, new_priority):
    with open(file_path, 'r') as file:
        content = file.read()
    content = re.sub(r'"m_Priority": \d+', f'"m_Priority": {new_priority}', content)

    with open(file_path, 'w') as file:
        file.write(content)

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_path = current_directory
prefab_files = [file for file in os.listdir(current_directory) if file.endswith('.Prefab')]

for index, file_name in enumerate(prefab_files, start=1):
    file_path = os.path.join(current_directory, file_name)
    replace_priority(file_path, index)
    print(f'Replaced priority value in {file_name} with {index}.')
import os

def process_prefab_file(file_path):
    with open(file_path, 'r') as f:
        prefab_text = f.read()

    index_rlength = prefab_text.find('"$rlength":')

    if index_rlength == -1:
        print(f"Error: \"$rlength\": not found in {file_path}. Skipping...")
        return

    prefab_text = prefab_text[:index_rlength + len('"$rlength":') + 1] + str(int(prefab_text[index_rlength + len('"$rlength":') + 1]) + 1) + prefab_text[index_rlength + len('"$rlength":') + 2:]
    index_rcontent = prefab_text.find('"$rcontent":')
    if index_rcontent == -1:
        print(f"Error: \"$rcontent\": not found in {file_path}. Skipping...")
        return

    new_component = '''
            {
                "$id": 8,
                "$type": "8|Game.Prefabs.UIObject, Game",
                "name": "UIObject",
                "active": true,
                "m_Group": $fstrref:CID:"13819b7e68a8fb4bc587d5e7c848181a",
                "m_Priority": 1,
                "m_Icon": "Media/Game/Icons/ZoneCommercial.svg",
                "m_LargeIcon": null,
                "m_IsDebugObject": false
            },'''
    prefab_text = prefab_text[:index_rcontent + len('"$rcontent":') + 2] + new_component + prefab_text[index_rcontent + len('"$rcontent":') + 2:]

    with open(file_path, 'w') as f:
        f.write(prefab_text)

    print(f"Processed: {file_path}")

def process_prefab_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.Prefab'):
            file_path = os.path.join(folder_path, file_name)
            process_prefab_file(file_path)

print(f"Starting...")
script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = script_dir
process_prefab_files_in_folder(folder_path)

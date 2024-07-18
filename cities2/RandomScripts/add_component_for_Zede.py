import os
import re

def read_prefab_files(directory):
    regex = re.compile(r' {4}"components": {\s*[\$\w": ,\s\|\.`\[\]]+ {8}"\$rlength": ([\d]+),\n {8}"\$rcontent": \[([\w\s{"\$:,\|\.\[\]/}]+)\n {8}]\n {4}},\n {4}"m_Meshes')
    regex2 = re.compile(r' {4}"components": {\s*[\$\w": ,\s\|\.`\[\]]+ {8}"\$rlength": ([\d]+)')
    for folder_name, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.Prefab'):
                file_path = os.path.join(folder_name, file_name)
                # print("COVanillaCarProps_AssetPack" in folder_name)
                with open(file_path, 'r') as f:
                    content = f.read()
                    match = regex.search(content)
                    match_l = regex2.search(content)
                    if match:
                        rlength = int(match.group(1))
                        rcontent = match.group(2)
                        content = re.sub(regex2, add_rlength, content)
                        content = content.replace(rcontent, add_identifier(file_name, rcontent))
                        rcontent = regex.search(content).group(2)
                        if "COVanillaCarProps_AssetPack" in folder_name:
                            rlength += 1
                            content = re.sub(regex2, add_rlength, content)
                            content = content.replace(rcontent, add_dlc(rcontent, 'cs1th'))
                        elif "SFVanillaCarProps_AssetPack" in folder_name:
                            rlength += 1
                            content = re.sub(regex2, add_rlength, content)
                            content = content.replace(rcontent, add_dlc(rcontent, 'sanfrancisco'))
                    content = content.replace('"UnityGUID:91c63b6825e22ec4b876ce7b52994f6b"','"CID:1137ea691f68745a3f25e82addc44ff0"')
                os.makedirs("D:\_Everything Else\Codes\Temp\out", exist_ok=True)
                os.makedirs(folder_name.replace("Temp\in","Temp\out"), exist_ok=True)
                with open(file_path.replace("Temp\in","Temp\out"), "w") as f:
                    f.write(content)


def add_rlength(match):
    rlength_value = int(match.group(1)) + 1
    full_match = match.group(0)
    replaced_match = re.sub(r'"\$rlength": [\d]+', f'"$rlength": {rlength_value}', full_match)
    return replaced_match

def add_identifier(name, rcontent):
    template = f""",
            {{
                "$id": 101,
                "$type": "101|Game.Prefabs.ObsoleteIdentifiers, Game",
                "name": "ObsoleteIdentifiers",
                "active": true,
                "m_PrefabIdentifiers": {{
                    "$id": 102,
                    "$type": "102|Game.Prefabs.PrefabIdentifierInfo[], Game",
                    "$rlength": 1,
                    "$rcontent": [
                        {{
                            "$id": 103,
                            "$type": "103|Game.Prefabs.PrefabIdentifierInfo, Game",
                            "m_Name": "Zede_{name.replace('.Prefab','')}",
                            "m_Type": "StaticObjectPrefab"
                        }}
                    ]
                }}
            }}"""
    return rcontent + template

def add_dlc(rcontent, dlc):
    match dlc:
        case 'cs1th':
            dlc_code = '39980c750d4c50b4ea7a7477b0411513'
        case 'paradox':
            dlc_code = '8e8e5bce147330542a1b89e4e96c2322'
        case 'landmark':
            dlc_code = 'c3724de73723f5b4ab589dd1fa756861'
        case 'sanfrancisco':
            dlc_code = '6a2dbb5b0d5ed814d975ec201667b644'
        case _:
            raise Exception("Invalid DLC")
    new_rcontent = f""",
            {{
                "$id": 111,
                "$type": "111|Game.Prefabs.ContentPrerequisite, Game",
                "name": "ContentPrerequisite",
                "active": true,
                "m_ContentPrerequisite": $fstrref:"UnityGUID:{dlc_code}"
            }}"""
    return rcontent + new_rcontent

if __name__ == "__main__":
    directory = "D:\_Everything Else\Codes\Temp\in" #os.getcwd()
    read_prefab_files(directory)
    
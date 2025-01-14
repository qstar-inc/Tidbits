import os
import json
import re

def clean_json(json_string):
    cleaned_json = re.sub(r'\$fstrref:"[^"]*"', 'null', json_string)
    cleaned_json = re.sub(r'([\d]+|"[\d]+\|UnityEngine.Color, UnityEngine.CoreModule"),\s*\d+.\d+,\s*\d+.\d+,\s*\d+.\d+,\s*\d+', '"null"', cleaned_json)
    return cleaned_json

def preprocess_json(json_string,filename):
    pattern = re.compile(r'(\n[ ]{8}\]\n[ ]{4}\},\n[ ]{4}"m_Sections": \{\n[ ]{8}"\$id":)')
    ui = f""",
            {{
                "$id": 1000,
                "$type": "1000|Game.Prefabs.EditorAssetCategoryOverride, Game",
                "name": "EditorAssetCategoryOverride",
                "active": true,
                "m_IncludeCategories": {{
                    "$id": 1001,
                    "$type": "1001|System.String[], mscorlib",
                    "$rlength": 1,
                    "$rcontent": [
                        "StarQ/Networks/{filename}"
                    ]
                }},
                "m_ExcludeCategories": {{
                    "$id": 1002,
                    "$type": 1001,
                    "$rlength": 0,
                    "$rcontent": [
                    ]
                }}
            }}"""
    preprocessed_json = pattern.sub(ui + r'\1', json_string)
    return preprocessed_json

def count_rcontent_in_json(json_string):
    rcontent_count = 0 

    try:
        cleaned_json_string = clean_json(json_string)
        data = json.loads(cleaned_json_string)
        if 'components' in data:
            components = data['components']
            if '$rcontent' in components:
                rcontent = components['$rcontent']
                rcontent_count = len(rcontent)
    except json.JSONDecodeError:
        print("json.JSONDecodeError")
    return rcontent_count

cwd = os.getcwd()

for root, dirs, files in os.walk(cwd):
    for filename in files:
        if filename.endswith('.Prefab'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as file:
                json_string = file.read()

            preprocessed_json_string = preprocess_json(json_string,filepath.replace(f"{cwd}\\","").split("\\")[0])
            with open(filepath, 'w') as file:
                file.write(preprocessed_json_string)
            rcontent_count = count_rcontent_in_json(preprocessed_json_string)

            with open(filepath, 'r') as file:
                file_lines = file.readlines()
            
            if rcontent_count != 0:
                if len(file_lines) >= 9:
                    file_lines[8] = f'        "$rlength": {rcontent_count},\n'
                
                with open(filepath, 'w') as file:
                    file.writelines(file_lines)
                print(f"File: {filename}, rcontent count: {rcontent_count}")

print("Files updated successfully.")

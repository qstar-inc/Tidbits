import os
import re
import json

resources = {
    0: "NoResource",
    1: "Money",
    2: "Grain",
    3: "ConvenienceFood",
    4: "Food",
    5: "Vegetables",
    6: "Meals",
    7: "Wood",
    8: "Timber",
    9: "Paper",
    10: "Furniture",
    11: "Vehicles",
    12: "Lodging",
    13: "UnsortedMail",
    14: "LocalMail",
    15: "OutgoingMail",
    16: "Oil",
    17: "Petrochemicals",
    18: "Ore",
    19: "Plastics",
    20: "Metals",
    21: "Electronics",
    22: "Software",
    23: "Coal",
    24: "Stone",
    25: "Livestock",
    26: "Cotton",
    27: "Steel",
    28: "Minerals",
    29: "Concrete",
    30: "Machinery",
    31: "Chemicals",
    32: "Pharmaceuticals",
    33: "Beverages",
    34: "Textiles",
    35: "Telecom",
    36: "Financial",
    37: "Media",
    38: "Entertainment",
    39: "Recreation",
    40: "Garbage",
    41: "Count / Last",
}

def find_pattern_in_prefab_files(root_dir):
    sold = re.compile(r'"m_AllowedSold": {[\s"$\w:,\|.\[\]]+"\$rlength": ([\d]+),\s*"\$rcontent": ([\[\]\s\w,]+)},')
    manu = re.compile(r'"m_AllowedManufactured": {[\s"$\w:,\|.\[\]]+"\$rlength": ([\d]+),\s*"\$rcontent": ([\[\]\s\w,]+)},')
    stor = re.compile(r'"m_AllowedStored": {[\s"$\w:,\|.\[\]]+"\$rlength": ([\d]+),\s*"\$rcontent": ([\[\]\s\w,]+)},')

    for folder_name, _, files in os.walk(root_dir):
        for file_name in files:
            if file_name.endswith('.Prefab'):
                file_path = os.path.join(folder_name, file_name)
                with open(file_path, 'r') as f:
                    content = f.read()
                    match1 = sold.search(content)
                    match2 = manu.search(content)
                    match3 = stor.search(content)
                    if match1:
                        rlength = int(match1.group(1))
                        rcontent = match1.group(2).replace('\n', '').replace(' ', '')
                        rcontent = json.loads(rcontent)
                        if rlength > 0:
                            rcontent_text = [resources.get(num, f"{num}") for num in rcontent]
                            print(f'{file_name} sells: {rcontent_text}')
                    if match2:
                        rlength = int(match2.group(1))
                        rcontent = match2.group(2).replace('\n', '').replace(' ', '')
                        rcontent = json.loads(rcontent)
                        if rlength > 0:
                            rcontent_text = [resources.get(num, f"{num}") for num in rcontent]
                            print(f'{file_name} manus: {rcontent_text}')
                    if match3:
                        rlength = int(match3.group(1))
                        rcontent = match3.group(2).replace('\n', '').replace(' ', '')
                        rcontent = json.loads(rcontent)
                        if rlength > 0:
                            rcontent_text = [resources.get(num, f"{num}") for num in rcontent]
                            print(f'{file_name} stors: {rcontent_text}')

# Example usage:
root_directory = 'C:/Users/Qoushik/AppData/LocalLow/Colossal Order/Cities Skylines II/StreamingData~/.Zones'  # Set your root directory here
find_pattern_in_prefab_files(root_directory)
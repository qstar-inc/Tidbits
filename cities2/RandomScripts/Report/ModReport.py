import os
import json

base_folder = os.path.expandvars(r'%LocalAppData%Low/Colossal Order/Cities Skylines II/.cache/Mods/mods_subscribed')
output_file = 'ModReport.txt'
report_lines = []

for root, dirs, files in os.walk(base_folder):
    if '.metadata' in dirs:
        metadata_path = os.path.join(root, '.metadata', 'metadata.json')
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                mod_id = metadata.get('Id', 'Unknown')
                display_name = metadata.get('DisplayName', 'Unknown')
                author = metadata.get('Author', 'Unknown')
                user_mod_version = metadata.get('UserModVersion', metadata.get('Version', 'Unknown'))
                report_line = f'{mod_id}: {display_name} ({user_mod_version}) [{author}]'
                report_lines.append(report_line)

with open(output_file, 'w', encoding='utf-8') as f:
    for line in report_lines:
        f.write(line + '\n')

print(f'Report generated: {os.getcwd()}\{output_file}')

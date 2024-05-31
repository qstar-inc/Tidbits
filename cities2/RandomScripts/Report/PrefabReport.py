import os
import re
import argparse
import time

def search_prefab_files(base_path):
    results = []
    name_regex = re.compile(r'"name":\s*"([^"]+)"')
    files_processed = 0

    start_time = time.time()

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith('.Prefab'):
                files_processed += 1
                relative_path = os.path.relpath(os.path.join(root, file), base_path)
                name_found = None

                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        match = name_regex.search(line)
                        if match:
                            name_found = match.group(1)
                            break
                try:
                    with open(os.path.join(root, file+'.cid'), 'r') as f2:
                        cid = f2.read().strip()
                except FileNotFoundError:
                    cid = "CID file missing"
                if name_found:
                    results.append(f"{relative_path}: {name_found} : {cid}")
                else:
                    results.append(f"{relative_path}: name not found : {cid}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    return results, elapsed_time, files_processed

def write_report(results, report_path):
    with open(report_path, 'w') as report_file:
        for result in results:
            report_file.write(result + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search .Prefab files for Cities Skylines II.')
    parser.add_argument('-outside', action='store_true', help='To use it outside the Cities Skylines II user data folder')
    args = parser.parse_args()
    base_path = os.getcwd().replace("\\","/")
    cs2_user_path = os.path.expandvars(r'%LocalAppData%Low/Colossal Order/Cities Skylines II').replace("\\","/")
    if os.path.expandvars(cs2_user_path) in base_path:
        go = True
    else:
        print("Hello from the other side!")
        print("This script is running from outside the Cities Skylines II user data folder.")
        if args.outside:
            go = True
        else:
            print("To use this script outside the Cities Skylines II user data folder, use the -outside argument. Like this:")
            print("python PrefabReport.py -outside")
            go = False

    if go == True:
        print("Creating report... This might take a while...")
        report_path = 'PrefabReport.txt'
        results, elapsed_time, files_processed = search_prefab_files(base_path)
        write_report(results, report_path)
        print(f"Report written to {report_path} for {files_processed} files in {elapsed_time:.2f} seconds.")
    else:
        print("Cancelling script execution")

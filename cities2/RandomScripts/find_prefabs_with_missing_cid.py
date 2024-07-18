import os

def log_prefab_files_without_cid(start_directory='.'):
    log_file_path = 'prefab_files_without_cid.log'
    files_logged = False  # Flag to check if any files were logged

    # Open a log file to write the paths of .Prefab files without .cid counterpart
    with open(log_file_path, 'w') as log_file:
        # Walk through all directories and subdirectories
        for root, dirs, files in os.walk(start_directory):
            for file in files:
                if file.endswith('.Prefab') or file.endswith('.cok'):
                    prefab_path = os.path.join(root, file)
                    cid_file = prefab_path + '.cid'
                    # Check if the corresponding .cid file exists
                    if not os.path.isfile(cid_file):
                        log_file.write(prefab_path + '\n')
                        files_logged = True
                        print(f"Logged: {prefab_path}")

    # Delete the log file if it is empty
    if not files_logged:
        os.remove(log_file_path)
        print(f"Log file {log_file_path} is empty and has been deleted.")
    else:
        print(f"Log file {log_file_path} has been created with entries.")

if __name__ == "__main__":
    log_prefab_files_without_cid()

import os
import shutil

def create_backup_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.cid'):
                cid_file_path = os.path.join(dirpath, filename)
                bak_file_path = cid_file_path + '.backup'
                shutil.copy(cid_file_path, bak_file_path)
                print(f'Created backup for {cid_file_path} as {bak_file_path}')

if __name__ == "__main__":
    current_directory = os.getcwd()
    create_backup_files(current_directory)
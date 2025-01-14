import os

def rename_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".Prefab.cid"):
                base_name = file[:-11]
                prefab_cid_path = os.path.join(subdir, file)
                with open(prefab_cid_path, 'r') as f:
                    content = f.read().strip()
                
                new_base_name = content
                new_prefab_cid_path = os.path.join(subdir, new_base_name + ".Prefab.cid")
                os.rename(prefab_cid_path, new_prefab_cid_path)
                
                prefab_file_path = os.path.join(subdir, base_name + ".Prefab")
                if os.path.exists(prefab_file_path):
                    new_prefab_file_path = os.path.join(subdir, new_base_name + ".Prefab")
                    os.rename(prefab_file_path, new_prefab_file_path)
                
                prefab_cid_backup_path = os.path.join(subdir, base_name + ".Prefab.cid.backup")
                if os.path.exists(prefab_cid_backup_path):
                    new_prefab_cid_backup_path = os.path.join(subdir, new_base_name + ".Prefab.cid.backup")
                    os.rename(prefab_cid_backup_path, new_prefab_cid_backup_path)

if __name__ == "__main__":
    root_dir = os.getcwd()
    rename_files(root_dir)

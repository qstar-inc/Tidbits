import os

def find_and_read_cid_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".cid"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    cid = f.read().strip()
                    print(f"{file}: {cid}")

# Specify the directory to start searching
directory_to_search = os.getcwd()
find_and_read_cid_files(directory_to_search)

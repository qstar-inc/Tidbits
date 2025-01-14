import os
import re
import csv

def read_csv(csv_filename):
    """Read the CSV file and return a dictionary mapping filenames to IDs."""
    filename_to_id = {}
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 2:
                continue
            filename, id_value = row
            filename_to_id[filename] = id_value
    return filename_to_id

def replace_mesh_id_in_file(filepath, new_id):
    """Replace the m_Mesh id in the given file with the new id."""
    with open(filepath, 'r') as file:
        content = file.read()

    pattern = r'"m_Mesh": \$fstrref:"([\w:]+)"'
    replacement = f'"m_Mesh": $fstrref:"CID:{new_id}"'
    new_content = re.sub(pattern, replacement, content)

    with open(filepath, 'w') as file:
        file.write(new_content)

def main():
    csv_filename = 'MeshID.csv'
    filename_to_id = read_csv(csv_filename)
    
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.Prefab'):
                filepath = os.path.join(root, file)
                if file in filename_to_id:
                    new_id = filename_to_id[file]
                    replace_mesh_id_in_file(filepath, new_id)
                    print(f'Replaced m_Mesh ID in {filepath} with CID:{new_id}')

if __name__ == '__main__':
    main()

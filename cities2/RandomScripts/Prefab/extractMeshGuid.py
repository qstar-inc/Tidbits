import os

def combine_cid_files():
    current_dir = os.getcwd()

    with open("extractMeshGuid.txt", "w") as combined_file:
        files = [file for file in os.listdir(current_dir) if file.endswith(".Prefab")]

        for file in files:
            with open(file, "r") as prefab_file:
                prefab_content = prefab_file.read()
                mesh = prefab_content.split('"m_Mesh": ')[1].split('"')[1]
                name = prefab_content.split('"name": "')[1].split('"')[0]
                combined_file.write(f"Mesh: {mesh}, Name: {name}\n")

    print("Combining complete!")

if __name__ == "__main__":
    combine_cid_files()


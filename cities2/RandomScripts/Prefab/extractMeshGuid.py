import os

def combine_cid_files():
    current_dir = os.getcwd()

    with open("extractMeshGuid.txt", "w") as combined_file:
        for dirpath, dirnames, filenames in os.walk(current_dir):
            for filename in filenames:
                if filename.endswith(".Prefab"):
                    with open(dirpath+'/'+filename, "r") as prefab_file:
                        prefab_content = prefab_file.read()
                        mesh_regex = prefab_content.split('"m_Mesh": ')
                        if len(mesh_regex)>1:
                            mesh = mesh_regex[1].split('"')[1]
                            name = prefab_content.split('"name": "')[1].split('"')[0]
                            combined_file.write(f"{name}.Prefab.cid: {mesh.replace("CID:","")}\n")

    print("Combining complete!")

if __name__ == "__main__":
    combine_cid_files()


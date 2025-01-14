import os

def combine_cid_files():
    current_dir = os.getcwd()
    with open("cidSaver.txt", "w") as combined_file:
        files = [file for file in os.listdir(current_dir) if file.endswith("Mesh.Prefab.cid")]
        # files = [file for file in os.listdir(current_dir) if file.endswith("png.cid")]
        
        for file in files:
            if not (file.endswith("LOD1 Mesh.Prefab.cid") or file.endswith("LOD2 Mesh.Prefab.cid")):
            # if not 1 == 2:    
                with open(file, "r") as cid_file:
                    file_contents = cid_file.read().strip()
                    combined_file.write(f"{file_contents}:00000000000000000000000000000000:{file.removesuffix(" Mesh.Prefab.cid")}\n")
    print("Combining complete!")

if __name__ == "__main__":
    combine_cid_files()
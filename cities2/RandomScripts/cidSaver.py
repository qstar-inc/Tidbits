import os

def combine_cid_files():
    current_dir = os.getcwd()
    with open("cidSaver.txt", "w") as combined_file:
        files = [file for file in os.listdir(current_dir) if file.endswith(".cid")]
        for file in files:
            with open(file, "r") as cid_file:
                file_contents = cid_file.read().strip()
                combined_file.write(file_contents + "\n")
    print("Combining complete!")

if __name__ == "__main__":
    combine_cid_files()
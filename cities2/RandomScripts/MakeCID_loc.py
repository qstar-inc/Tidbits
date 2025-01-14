import os
import xxhash

def generate_guid(text):
    encoded_text = text.encode('utf-16le')
    hash128 = xxhash.xxh3_128(encoded_text).digest()
    hash_hex = hash128.hex()
    return hash_hex

def process_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".loc"):
                prefab_path = os.path.join(subdir, file)
                cid_path = f"{prefab_path}.cid"
                
                if not os.path.exists(cid_path):
                    guid = generate_guid("StarQ:" + file)
                    with open(cid_path, 'w') as cid_file:
                        cid_file.write(guid)
                    print(f'Generated GUID for {prefab_path} and saved as {cid_path}')

if __name__ == "__main__":
    root_directory = os.getcwd()
    process_files(root_directory)

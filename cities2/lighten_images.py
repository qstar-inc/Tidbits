import os
import subprocess

def lighten_images_and_rename():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'image.png':
                original_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, '_BaseColorMap.png')
                print(f"Processing: {original_file_path} -> {new_file_path}")
                command = ['magick', 'convert', original_file_path, '-modulate', '70,70', new_file_path]
                subprocess.run(command)

if __name__ == "__main__":
    lighten_images_and_rename()

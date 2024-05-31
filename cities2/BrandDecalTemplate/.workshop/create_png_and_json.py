import csv
import json
import os
from PIL import Image, ImageDraw

def create_folders_and_images_from_tsv(tsv_file):
    output_folder = os.path.join(os.path.dirname(tsv_file), 'output')
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(os.path.join(output_folder, '.assets'), exist_ok=True)
    
    with open(tsv_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) == 1:
                row = row[0].strip('"')
                name, resolution, lx, ly, lz = row.split('\t')
                width, height = map(int, resolution.split('x'))
                lx, ly, lz = float(lx), float(ly), float(lz)
                
                folder_path = os.path.join(output_folder, name)
                os.makedirs(folder_path, exist_ok=True)
                make_json(folder_path, lx, ly, lz)
                make_image(folder_path, name, width, height)

def make_json(folder_path, lx, ly, lz):
    json_path = os.path.join(folder_path, 'decal.json')
    data = {
                "Float": {
                    "_Metallic": 0,
                    "_Smoothness": 0,
                    "colossal_DecalLayerMask": 36,
                    "_NormalOpacity": 2,
                    "_MetallicOpacity": 0,
                    "UiPriority": 1980100
                },
                "Vector": {
                    "colossal_MeshSize": {
                        "x": lx,
                        "y": lz,
                        "z": ly,
                        "w": 0
                    },
                    "colossal_TextureArea": {
                        "x": 0,
                        "y": 0,
                        "z": 1,
                        "w": 1
                    }
                }
            }
    
    with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)
            
def make_image(folder_path, name, width, height):
    image_path = os.path.join(folder_path, f'image.png')
    if name.endswith('_Top'):
        create_semicircle_image(image_path, width, height)
    elif 'Round' in name:
        create_circle_image(image_path, width, height)
    else:
        create_white_image(image_path, width, height)
    

def create_white_image(image_path, width, height):
    image = Image.new('RGBA', (width, height), color='white')
    image.save(image_path)

def create_semicircle_image(image_path, width, height):
    n = 4
    image = Image.new('RGBA', (width * n, height * n), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    bbox = [0, 0, width * n, height * n * 2]
    draw.pieslice(bbox, 180, 360, fill='white')
    image = image.resize((width, height))
    image.save(image_path)

def create_circle_image(image_path, width, height):
    n = 4
    width, height = width * n, height * n
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    bbox = [(width - height) // 2, 0, (width + height) // 2, height] if width > height else [0, (height - width) // 2, width, (height + width) // 2]
    draw.ellipse(bbox, fill='white')
    image = image.resize((int(width / n), int(height / n)))
    image.save(image_path)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    tsv_file = os.path.join(script_dir, 'raw.tsv')
    if os.path.exists(tsv_file):
        create_folders_and_images_from_tsv(tsv_file)
    else:
        print(f"File {tsv_file} does not exist.")

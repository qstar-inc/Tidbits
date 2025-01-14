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
                name, rect_res, resolution, lx, ly, lz = row.split('\t')
                width, height = map(int, resolution.split('x'))
                rect_width, rect_height = map(int, rect_res.split('x'))
                lx, ly, lz = float(lx), float(ly), float(lz)
                
                folder_path = os.path.join(output_folder, name)
                os.makedirs(folder_path, exist_ok=True)
                make_json(folder_path, lx, ly, lz)
                make_image(folder_path, name, width, height, rect_width, rect_height)

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
            
def make_image(folder_path, name, width, height, rect_width, rect_height):
    image_path = os.path.join(folder_path, f'image.png')
    if name.endswith('_Top'):
        create_semicircle_image(image_path, width, height, rect_width, rect_height)
    elif 'Round' in name or 'SignSidewaySmall02' in name:
        create_circle_image(image_path, width, height, rect_width, rect_height)
    else:
        create_white_image(image_path, width, height, rect_width, rect_height)
    

def create_white_image(image_path, width, height, rect_width, rect_height):
    image = Image.new('RGBA', (rect_width, rect_height), (0, 0, 0, 0))

    draw = ImageDraw.Draw(image)
    x1 = (rect_width - width) // 2
    y1 = (rect_height - height) // 2
    x2 = x1 + width
    y2 = y1 + height
    draw.rectangle([x1, y1, x2, y2], fill='white')
    image.save(image_path)


def create_semicircle_image(image_path, width, height, rect_width, rect_height):
    n = 4
    image = Image.new('RGBA', (rect_width * n, rect_height * n), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    x1 = (rect_width * n - width * n) // 2
    print(x1)
    y1 = (rect_height * n - height * n) * 2
    print(y1)
    x2 = x1 + width * n
    print(x2)
    y2 = y1 + height * n * 2
    print(y2)

    bbox = [x1, y1, x2, y2]
    draw.pieslice(bbox, 180, 360, fill='white')

    image = image.resize((rect_width, rect_height))
    image.save(image_path)


def create_circle_image(image_path, width, height, rect_width, rect_height):
    n = 4
    rect_width, rect_height = rect_width * n, rect_height * n
    width, height = width * n, height * n

    image = Image.new('RGBA', (rect_width, rect_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    if width == height:
        bbox = [
            (rect_width - width) // 2,
            (rect_height - height) // 2,
            (rect_width + width) // 2,
            (rect_height + height) // 2,
        ]
    else:
        print(f"Not circular: {image_path}")

    draw.ellipse(bbox, fill='white')

    image = image.resize((rect_width // n, rect_height // n))
    image.save(image_path)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    tsv_file = os.path.join(script_dir, 'raw.tsv')
    if os.path.exists(tsv_file):
        create_folders_and_images_from_tsv(tsv_file)
    else:
        print(f"File {tsv_file} does not exist.")

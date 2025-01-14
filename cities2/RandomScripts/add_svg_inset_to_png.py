from PIL import Image, ImageDraw, ImageOps
import cairosvg
import os
import io

def combine_images(png_path, svg_path, output_path, inset_size=(100, 100), position=(10, 10), offset = (3, 2), square_size=(58, 58), square_color="#001626", border_color="#3152ff", border_width=3):
    base_image = Image.open(png_path).convert("RGBA")
    rounded_square = Image.new("RGBA", square_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(rounded_square)

    radius = 10
    rect = [border_width, border_width, square_size[0] - border_width, square_size[1] - border_width]
    draw.rounded_rectangle(rect, radius, fill=square_color, outline=border_color, width=border_width)

    inset_image_data = cairosvg.svg2png(url=svg_path, output_width=inset_size[0], output_height=inset_size[1])
    inset_image = Image.open(io.BytesIO(inset_image_data)).convert("RGBA")

    inset_position = (base_image.width - inset_size[0] - position[0] - offset[0], base_image.height - inset_size[0] - position[1] - offset[1])
  
    if "Adult" in svg_path:
        svg_positionX = (
                inset_position[0] + (square_size[0] - inset_size[0]) // 2 + 4,
                inset_position[1] + (square_size[1] - inset_size[1]) // 2 + 1
        )
    else:
        svg_positionX = (
                inset_position[0] + (square_size[0] - inset_size[0]) // 2 + 1,
                inset_position[1] + (square_size[1] - inset_size[1]) // 2 + 3
        )
    base_image.paste(rounded_square, inset_position, rounded_square)
    base_image.paste(inset_image, svg_positionX, inset_image)
    base_image.save(output_path)

def process_images(png_dir, svg_dir, output_dir, inset_size=(50, 50), position=(5, 5)):
    os.makedirs(output_dir, exist_ok=True)
    
    for png_file in os.listdir(png_dir):
        if png_file.endswith(".png"):
            png_path = os.path.join(png_dir, png_file)
            png_name = os.path.splitext(png_file)[0]

            for svg_file in os.listdir(svg_dir):
                if svg_file.endswith(".svg"):
                    svg_path = os.path.join(svg_dir, svg_file)
                    svg_name = os.path.splitext(svg_file)[0]

                    output_file = f"{png_name}_{svg_name}.png"
                    output_path = os.path.join(output_dir, output_file)

                    combine_images(png_path, svg_path, output_path, inset_size, position)

process_images("png", "svg", "output")

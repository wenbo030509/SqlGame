import os
import math
import subprocess
import struct
import shutil
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ICONSET_DIR = os.path.join(SCRIPT_DIR, "icon.iconset")


def create_base_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    bg_color = (41, 98, 255)
    corner_radius = int(size * 0.22)

    draw.rounded_rectangle(
        [(0, 0), (size - 1, size - 1)],
        radius=corner_radius,
        fill=bg_color,
    )

    text = "SQL"
    try:
        font_size = int(size * 0.32)
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except (OSError, IOError):
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except (OSError, IOError):
            font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = (size - text_w) // 2
    text_y = (size - text_h) // 2 - int(size * 0.04)

    shadow_color = (20, 60, 180)
    draw.text((text_x + 1, text_y + 1), text, fill=shadow_color, font=font)
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

    return img


def generate_ico():
    ico_path = os.path.join(SCRIPT_DIR, "icon.ico")
    sizes = [256, 128, 64, 48, 32, 24, 16]

    base = create_base_icon(max(sizes))
    resized_images = []
    for s in sizes:
        resized_images.append(base.resize((s, s), Image.LANCZOS))

    resized_images[0].save(
        ico_path,
        format="ICO",
        sizes=[(s, s) for s in sizes],
        append_images=resized_images[1:],
    )
    print(f"  ✅ icon.ico generated ({', '.join(f'{s}x{s}' for s in sizes)})")


def generate_icns(sizes):
    os.makedirs(ICONSET_DIR, exist_ok=True)

    base = create_base_icon(1024)

    iconset_map = [
        ("icon_16x16.png", 16),
        ("icon_16x16@2x.png", 32),
        ("icon_32x32.png", 32),
        ("icon_32x32@2x.png", 64),
        ("icon_128x128.png", 128),
        ("icon_128x128@2x.png", 256),
        ("icon_256x256.png", 256),
        ("icon_256x256@2x.png", 512),
        ("icon_512x512.png", 512),
        ("icon_512x512@2x.png", 1024),
    ]

    for filename, size in iconset_map:
        img = base.resize((size, size), Image.LANCZOS)
        img.save(os.path.join(ICONSET_DIR, filename), "PNG")

    icns_path = os.path.join(SCRIPT_DIR, "icon.icns")
    subprocess.run(
        ["iconutil", "-c", "icns", ICONSET_DIR, "-o", icns_path],
        check=True,
        capture_output=True,
    )

    os_sizes = sorted(set(s for _, s in iconset_map))
    print(f"  ✅ icon.icns generated ({', '.join(f'{s}x{s}' for s in os_sizes)} @1x/@2x)")


def main():
    print("🎨 Generating icons for SQL Learning Client...")
    generate_ico()
    generate_icns(1024)
    shutil.rmtree(ICONSET_DIR)
    print("🎉 All icons generated successfully!")


if __name__ == "__main__":
    main()

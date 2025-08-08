#!/usr/bin/env python3
import os
import re
from PIL import Image

def images_to_pdf(folder, output_pdf="Rockfort Robotics Pitch Deck.pdf"):
    # Gather image files
    files = os.listdir(folder)
    imgs = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'))]
    if not imgs:
        raise RuntimeError("No image files found in " + folder)

    # Sort numerically
    def key_fn(fn):
        base = os.path.splitext(fn)[0]
        m = re.match(r'(\d+)$', base)
        return int(m.group(1)) if m else base
    imgs.sort(key=key_fn)

    # Load, resize, and convert to RGB
    pages = []
    for img_name in imgs:
        img = Image.open(os.path.join(folder, img_name))
        img = img.convert("RGB")
        # Resize to 50%
        img = img.resize((img.width // 2, img.height // 2), Image.LANCZOS)
        pages.append(img)

    # Save as PDF
    first, rest = pages[0], pages[1:]
    out_path = os.path.join(folder, output_pdf)
    first.save(out_path, "PDF", save_all=True, append_images=rest)
    print(f"→ {out_path} ({len(pages)} pages)")

if __name__ == "__main__":
    cwd = "C:\\Users\\abhis\\OneDrive\\Desktop\\Rockfort Robotics Pre-Seed Pitch Deck US and Off the Shelf modified\\pitch_images"
    images_to_pdf(cwd)

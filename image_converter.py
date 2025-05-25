#!/usr/bin/env python3


from PIL import Image, UnidentifiedImageError

import os



source_dir = os.path.expanduser("~/images")

dest_dir = "/opt/icons"

os.makedirs(dest_dir, exist_ok=True)



for filename in os.listdir(source_dir):

    file_path = os.path.join(source_dir, filename)

    if os.path.isfile(file_path):

        try:

            with Image.open(file_path) as img:

                new_img = img.rotate(-90).resize((128, 128)).convert("RGB")

                new_filename = filename + ".jpeg"

                new_path = os.path.join(dest_dir, new_filename)

                new_img.save(new_path, "JPEG")

        except UnidentifiedImageError:

            print(f"Skipping non-image file: {filename}")

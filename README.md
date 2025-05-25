# Image Converter for Web Icons

This project was developed as part of a Python automation lab using the Pillow library.

## Description

The script automates the following tasks for a batch of `.tiff` images provided by a web design contractor:
- Rotates each image 90 degrees clockwise
- Resizes them from 192x192 to 128x128 pixels
- Converts them to JPEG format
- Saves them to the `/opt/icons` directory

## Technologies Used

- Python 3
- Pillow (Python Imaging Library)

## How to Run

1. Place `.tiff` images in the `~/images/` directory.
2. Ensure the `/opt/icons/` directory is accessible.
3. Run the script:

```bash
python3 image_converter.py
```

Converted images will appear in `/opt/icons`.

## Author

Bekzod Ochilov

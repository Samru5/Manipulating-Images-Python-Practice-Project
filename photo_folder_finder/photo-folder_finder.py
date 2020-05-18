#photo_folder_finder.py
#A program identifying Photo Folders on the Hard Drive

import os

"""Python Imaging Library. Python Imaging Library (abbreviated as PIL) (in newer versions known as Pillow) is a free
 and open-source additional library for the Python programming language that adds support for opening, 
 manipulating, and saving many different image file formats."""
from PIL import Image

#Method takes root directory path to search photo folders
def find(root):

    #Walks through tree of given path
    for foldername, subfolders, filenames in os.walk(root):
        numPhotoFiles = 0
        numNonPhotoFiles = 0
        for filename in filenames:
            # Check if file extension is not .png or .jpg.
            if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
                numNonPhotoFiles += 1
                continue    # skip to next filename

            # Open image file using Pillow.
            try:
                im = Image.open(os.path.join(foldername, filename))
            except OSError:
                continue

            width, height = im.size

            """Check if width & height are larger than 500.
            (Photo file’s width and height must both be larger than 500 pixels.)"""
            if width > 500 and height > 500:
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1

        # If more than half of files were photos,
        # print the absolute path of the folder.
        if numPhotoFiles > numNonPhotoFiles:
            print(os.path.abspath(foldername))


if __name__ == "__main__":
    find('/')
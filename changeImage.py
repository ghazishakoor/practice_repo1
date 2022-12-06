#!/usr/bin/env python3

import os
from PIL import Image

path = "./supplier-data/images/"
new_size = (600, 400)

filenames = [f for f in os.listdir(path) if f.endswith(".tiff")]
for file in filenames:
    im = Image.open(path + file)
    new_im = im.convert("RGB").resize(new_size)
    file, ext = file.split(".")
    new_im.save(path + file + ".jpeg")
        

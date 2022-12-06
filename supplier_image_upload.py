#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
img_path = './supplier-data/images/'

filenames = [f for f in os.listdir(img_path) if f.endswith(".jpeg")]

for name in filenames:
    with open(img_path + name, 'rb') as opened:
        r = requests.post(url, files={"file": opened})

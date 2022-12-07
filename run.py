#!/usr/bin/env python3

from os import listdir, path
import requests
import json

# Extract image_names from the text file names

image_names = []
url = "http://localhost/fruits/"
imagepath = "./supplier-data/images/"
filepath = "./supplier-data/descriptions/"

txtfilenames = [f for f in listdir(filepath) if f.endswith(".txt")]

for name in txtfilenames:
    img_name, ext = name.split(".")
    image_name = img_name + ".jpeg"
    image_names.append(image_name)

    # Extract data fields from the text files

    with open(filepath + name) as f:
        lines = f.read().strip().splitlines()
        name, weight, description = lines

        # Extract integer value of weight from the string weight
    
        weight = int(weight.replace(" lbs", ""))

    # Create the data object
    keys = ["name", "weight", "description", "image_name"]
    vals = [name, weight, description, image_name]
    
    data = dict(zip(keys,vals))
    
    response = requests.post(url, data=data)
    if response.ok:
        print("data uploaded ok")
    else:
        print(f"error: {response.status_code}")
        


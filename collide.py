#!/usr/bin/env python3
# DESCRIPTION: scale and format files correctly
import os
import secrets
import subprocess
import sys
from pathlib import Path
from PIL import Image

a1, a2 = sys.argv[1:3]

i1 = Image.open(a1)
i2 = Image.open(a2)

img_format = "RGBA"
size = max(i1.size, i2.size) # select largest image and scale it to that (images have to have same dimensions and format otherwise pngStd wont work)

i1 = i1.convert(img_format)
i2 = i2.convert(img_format)

i1 = i1.resize(size)
i2 = i2.resize(size)

new_ext = str(secrets.token_hex()[:16])

i1.save((a1_new := f"{a1.split(".")[0]}_{new_ext}.png"))
i2.save((a2_new := f"{a2.split(".")[0]}_{new_ext}.png"))

subprocess.run(["python3", "pngStd.py", a1_new, a2_new], check = True)

for path in Path().glob("*.bin"):
	if path.is_file():
		path.unlink()

os.remove(a1_new)
os.remove(a2_new)
os.remove("prefix")

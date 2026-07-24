#!/usr/bin/env python3
import os
import glob
import secrets
import shutil
import subprocess

random_name = lambda : secrets.token_hex()[:(7 + secrets.randbelow(12 - 7))] + ".png"
pairs_dir = "pairs_2"
skip = False # skip if already exists

os.makedirs(pairs_dir, exist_ok = True)

for index, (evil, good) in enumerate(zip(os.listdir("evil"), os.listdir("good"))):
	pairs = os.path.join(pairs_dir, str(index))

	if os.path.exists(pairs) and skip:
		continue

	os.makedirs(pairs, exist_ok = True)

	try:
		subprocess.run([
			"python3",
			"collide.py",
			os.path.join("evil/", evil),
			os.path.join("good/", good)
		], check = True)
	except KeyboardInterrupt:
		shutil.rmtree(pairs)

	shutil.copyfile(
		(evil := glob.glob("*-evil.png")[0]),
		os.path.join(pairs, random_name())
	)
	shutil.copyfile(
		(good := glob.glob("*-good.png")[0]),
		os.path.join(pairs, random_name())
	)
	os.remove(evil)
	os.remove(good)

init:
	pip3 install -r requirements.txt

start:
	python3 bell-peppers-and-beef/core.py

fix:
	pip3 install -r requirements.txt
	autopep8 --recursive --aggressive --in-place bell-peppers-and-beef

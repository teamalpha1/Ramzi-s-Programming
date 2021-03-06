from time import sleep
from os import system
import platform
import sys

hertz = 60

if platform.system() == "Windows":
    clear_word = "cls"
else:
    clear_word = "clear"

blank = [
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0]
		]

box = 	[
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1]
		]

E = 	[
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1]
		]

message =	[
			[1,1,0,0,1,0,0,0,0,0],
			[1,0,0,1,0,1,0,0,0,0],
			[1,1,0,1,1,1,0,0,0,0],
			[1,0,0,1,0,1,0,0,0,0],
			[1,1,0,1,0,1,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0]
			]


def refreshScreen(display):
	system(clear_word)
	for line in display:
		for pixel in line:
			sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n")

refreshScreen(blank)
refreshScreen(box)
refreshScreen(E)
refreshScreen(message)
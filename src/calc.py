import os
import time


def digitaldatatypes():
	print(" - Bit (b) – the smallest unit, either 0 or 1.")
	print(" - Conversion: 8 bits = 1 byte")
	print(" - Byte (B) – 8 bits.")
	print(" - Conversion: 1 B = 8 b")
	print(" - Kilobyte (KB) – 1024 bytes")
	print(" - Conversion: 1 KB = 1024 B")
	print(" - Megabyte (MB) – 1024 KB")
	print(" - Conversion: 1 MB = 1024 KB")
	print(" - Gigabyte (GB) – 1024 MB")
	print(" - Conversion: 1 GB = 1024 MB")
	print(" - Terabyte (TB) – 1024 GB")
	print(" - Conversion: 1 TB = 1024 GB")
	print(" - Petabyte (PB) – 1024 TB")
	print(" - Conversion: 1 PB = 1024 TB")
	print("")

def convert():
	print("Data to convert from")
	global datatype1
	datatype1 = input("> ").upper()
	print("")

	print("Data to convert to")
	global datatype2
	datatype2 = input("> ").upper()
	print("")

	print(f"Number of {datatype1}")
	global number1
	number1 = float(input("> "))
	print("")

	# conversion table (all values relative to bytes)
	units = {
		"B": 1,
		"KB": 1024,
		"MB": 1024**2,
		"GB": 1024**3,
		"TB": 1024**4,
		"PB": 1024**5,
		"b": 1/8
	}

	global con_ans
	if datatype1 in units and datatype2 in units:
		bytes_value = number1 * units[datatype1]
		con_ans = bytes_value / units[datatype2]
		print(f"Conversion: {con_ans}")
	else:
		con_ans = "Invalid data type"
		print(f"Conversion: {con_ans}")


def clear():
	os.system('cls')

def help():
	print("Available commands")
	print(" - leave")
	print(" - convert")
	print(" - clear")
	print(" - types")
	print("")

def com():
	global command
	command=input("> ")

def autoexec():
	for _ in range(5):
		print(".")
		time.sleep(0.25)
		clear()
		time.sleep(0.25)
	time.sleep(2)
	print("Importing modules")
	time.sleep(2)
	print("Loading commands")
	time.sleep(1.5)
	print("Loading app")
	time.sleep(3.5)
	clear()
	print("CON CALC 2026 - Kyle Marko James Keightley")
	print("WELCOME TO CON CALC v1.0! TYPE ""help"" to see all available commands")
	print("")

autoexec()
running=True
while running:
	com()
	
	if command == "leave":
		running=False

	if command == "clear":
		clear()
		
	if command == "help":
		help()

	if command == "types":
		digitaldatatypes()

	if command == "convert":
		convert()
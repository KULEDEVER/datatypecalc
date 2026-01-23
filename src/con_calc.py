import os
import time

def convert_unit_weight():

def digitaldatatypes():
	print("Listing all available")
	print(" ╠═Bit (b)")
	print(" ╠═Byte (B)")
	print(" ╠═Kilobyte (KB)")
	print(" ╠═Megabyte (MB)")
	print(" ╠═Gigabyte (GB)")
	print(" ╠═Terabyte (TB)")
	print(" ╚═Petabyte (PB)")
	print("")

def convert_digital_data():
	print("Data to convert from")
	global datatype1
	datatype1 = input("Data Type> ").upper()
	print("")

	print("Data to convert to")
	global datatype2
	datatype2 = input("Data Type> ").upper()
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
#╚╠═
def list_unit_types():
	print(" ╠═Data")
	print(" ╚═Weight")
	print("")

def weight_units():
	print(" ╠═Metric")
	print(" ╚═Imperial")

def convert():
	print("What unit do you want?")
	list_unit_types()
	global ask_unit_type
	ask_unit_type=input("Unit Type> ")

	if ask_unit_type == "data":
		convert_digital_data()

	if ask_unit_type == "weight":
		weight_units()
		global ask_weight_unit_type
		ask_weight_unit_type=input("Weight Unit")

		if ask_weight_unit_type == "metric":
			convert_unit_weight()

		if ask_weight_unit_type == "imperial":
			convert_unit_weight()


def clear():
	os.system('cls')

def help():
	print("Listing all available commands")
	print(" ╠═leave - leave the app")
	print(" ╠═convert - convert one unit to the other")
	print(" ╠═clear - clear the screen")
	print(" ╚═types - check all available unit types")
	print("")

def com():
	global command
	command=input("CON CALC> ")

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
	print("WELCOME TO CON CALC v1.1! TYPE ""help"" to see all available commands")
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

	if command == "LEAVE":
		running=False

	if command == "CLEAR":
		clear()
		
	if command == "HELP":
		help()

	if command == "TYPES":
		digitaldatatypes()

	if command == "CONVERT":
		convert()
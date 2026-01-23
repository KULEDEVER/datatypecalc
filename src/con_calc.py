import os
import time

def convert_unit_weight():
    # Arrays of units with values relative to grams
    imperial = [
        ("grain", "gr", 0.06479891),
        ("dram", "dr", 1.7718451953125),
        ("ounce", "oz", 28.3495),
        ("pound", "lb", 453.592),
        ("stone", "st", 6350.29),
        ("quarter", "qr", 12700.58),
        ("hundredweight", "cwt", 50802.34)
    ]

    metric = [
        ("milligram", "mg", 0.001),
        ("centigram", "cg", 0.01),
        ("decigram", "dg", 0.1),
        ("gram", "g", 1),
        ("dekagram", "dag", 10),
        ("hectogram", "hg", 100),
        ("kilogram", "kg", 1000)
    ]

    # Combine all units into a single dictionary for easy lookup
    units = {abbr: value for name, abbr, value in imperial + metric}

    # User input
    print("Weight unit to convert from:")
    weight1 = input("Weight Unit> ").lower()
    print("Weight unit to convert to:")
    weight2 = input("Weight Unit> ").lower()
    print(f"Amount in {weight1}:")
    number = float(input("> "))

    # Check if units are valid
    if weight1 not in units or weight2 not in units:
        print(f"Invalid unit. Available units: {list(units.keys())}")
        return

    # Convert to grams first
    value_in_grams = number * units[weight1]

    # Convert from grams to target unit
    converted_value = value_in_grams / units[weight2]

    print(f"{number} {weight1} is equal to {converted_value} {weight2}")

def digitaldatatypes():
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
	digitaldatatypes()
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

def convert():
	print("What unit do you want?")
	list_unit_types()
	global ask_unit_type
	ask_unit_type=input("Unit Type> ")

	if ask_unit_type == "data":
		convert_digital_data()

	if ask_unit_type == "weight":
		convert_unit_weight()


def clear():
	os.system('cls')

def help():
	print("Listing all available commands")
	print(" ╠═leave - leave the app")
	print(" ╠═convert - convert one unit to the other")
	print(" ╚═clear - clear the screen")
	print("")

def com():
	global command
	command=input("CON CALC> ")

def autoexec():
	print("Loading app")
	time.sleep(1)
	clear()
	print("CON CALC 2026 - KULEDEVER")
	print("WELCOME TO CON CALC v1.2! TYPE help to see all available commands")
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

	if command == "convert":
		convert()

	if command == "LEAVE":
		running=False

	if command == "CLEAR":
		clear()
		
	if command == "HELP":
		help()

	if command == "CONVERT":
		convert()
from flight import *

input_file_name = "input.json"

with open(input_file_name, 'r') as file:
	input_json=file.readlines()

flights = FlightList()

flights.read_json(input_json)
	
flights.print()


while True:
	print("---------------------")
	print("What do you want:")
	print("1) Sort by parameter")
	print("2) Find flight")
	print("3) Delete by index")
	print("4) Add an flight")
	print("5) Edit an flight")
	x = input()
	try:
		x = int(x)
	except:
		continue
	if (x>7 or x<1):
		continue
	if (x==1):
		sort_param = input("Input name of sort parameter: ")
		flights.sort(sort_param)

	if (x==2):
		print("Input something")
		search_str = input()
		try:
			flights.find_flight(search_str).print()
		except:
			print("didn't find")
	if (x==3):
		ind = int(input("Input index: "))
		flights.delete(int(ind))
	if (x==4):
		flights.add()
	if (x==5):
		flights.edit()

	flights.save_to_json(input_file_name)
	if (x!=2):
		flights.print()
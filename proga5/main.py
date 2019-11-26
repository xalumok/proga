from adress import *

input_file_name = "input.json"

with open(input_file_name, 'r') as file:
	input_json=file.readlines()

adresses = AdressList()

adresses.read_json(input_json)
	
adresses.print()


while True:
	print("---------------------")
	print("What do you want:")
	print("1) Sort by parameter")
	print("2) Find adress")
	print("3) Delete by index")
	print("4) Add an adress")
	print("5) Edit an adress")
	x = input()
	try:
		x = int(x)
	except:
		continue
	if (x>7 or x<1):
		continue
	if (x==1):
		sort_param = input("Input name of sort parameter: ")
		adresses.sort(sort_param)

	if (x==2):
		print("Input something")
		search_str = input()
		try:
			adresses.find_adress(search_str).print()
		except:
			print("didn't find")
	if (x==3):
		ind = int(input("Input index: "))
		adresses.delete(int(ind))
	if (x==4):
		adresses.add()
	if (x==5):
		adresses.edit()

	adresses.save_to_json(input_file_name)
	if (x!=2):
		adresses.print()
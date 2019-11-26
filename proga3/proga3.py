import json


class Adress:
	def __init__(self):
		self.surname = ""
		self.street_name = ""
		self.house_num = -1

	def reader(self, input_dict, *kwargs):
		for key in input_dict:
			try:
				setattr(self, key, input_dict[key])
			except:
				print("Wrong input JSON")
				exit(0)
	def validate(self):
		if type(self.surname) is not str:
			return False
		elif not self.surname.isalpha():
			return False

		if type(self.surname) is not str:
			return False
		elif not self.surname.isalpha():
			return False

		if type(self.house_num) is not int:
			return False
		elif self.house_num < 0:
			return False
		return True

	def print(self):
		print("Adress{ Surname: ", self.surname, ", Street: " + self.street_name + ", House number: " + str(self.house_num) + "}")


def sort_by_surname(adr_list):
	get_surname = lambda adr: adr.surname
	adr_list.sort(key = get_surname)

def sort_by_street(adr_list):
	get_street = lambda adr: adr.street_name
	adr_list.sort(key = get_street)

def sort_by_house_num(adr_list):
	get_house_num = lambda adr: adr.house_num
	adr_list.sort(key = get_house_num)


def find_by_surname(adr_list, search_surname):
	for adr in adr_list:
		if adr.surname == search_surname:
			return adr
	return NULL

with open("input.json", 'r') as file:
	input_json=file.readlines()

adresses = []

for x in input_json:
	cur_adr = Adress()
	try:
		cur_adr.reader(json.loads(x))
		if (cur_adr.validate()):
			adresses.append(cur_adr)
		else:
			print("bad input")
	except:
		print('bad input')
	

for x in adresses:
	x.print()

while True:
	print("---------------------")
	print("What do you want:")
	print("1) Sort by surname")
	print("2) Sort by street name")
	print("3) Sort by house number")
	print("4) Find by surname")
	x = input()
	try:
		x = int(x)
	except:
		continue
	if (x>4 or x<1):
		continue
	if (x==1):
		sort_by_surname(adresses)
	if (x==2):
		sort_by_street(adresses)
	if (x==3):
		sort_by_house_num(adresses)
	if (x==4):
		print("Input surname")
		surname = input()
		try:
			find_by_surname(adresses, surname).print()
		except:
			print("didn't find")
	if (x!=4):
		for x in adresses:
			x.print()
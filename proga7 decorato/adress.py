import json
from decorators import *
class Adress:
	def __init__(self):
		self.surname = ""
		self.street_name = ""
		self.house_num = -1
		self.floor_num = -1
		self.apart_num = -1

	def reader(self, input_dict, *kwargs):
		for key in input_dict:
			try:
				setattr(self, key, input_dict[key])
			except:
				print("Wrong input JSON")
				exit(0)

	def validate(self):
		if not self.surname.isalpha():
			return False
		if not self.street_name.isalpha():
			return False
		try:
			self.house_num = int(self.house_num)
			if self.house_num <= 0:
				return False
		except:
			return False
		try:
			self.floor_num = int(self.floor_num)
			if self.floor_num <= 0:
				return False
		except:
			return False
		try:
			self.apart_num = int(self.apart_num)
			if self.apart_num <= 0:
				return False
		except:
			return False
		return True

	def print(self):
		print(self.__dict__)


class AdressList:
	def __init__(self):
		self.adresses = []


	def read_json(self, input_json):
		for x in input_json:
			cur_adr = Adress()
			cur_adr.reader(json.loads(x))
			self.add(cur_adr)


	def add(self):
		print("Input values in this order", str(list(Adress().__dict__.keys())))
		info = input().split()
		self.add_from_info(info)
		
	@check_add_info
	def add_from_info(self, info):
		new_adr = Adress()
		ind = 0
		for key in new_adr.__dict__.keys():
			setattr(new_adr, key, info[ind])
			ind += 1
		self.add(new_adr)

	@check_adress
	def add(self, new_adr):
		self.adresses.append(new_adr)

	@check_index
	def delete(self, ind):
		del self.adresses[ind]

	def edit(self):
		ind = int(input("Input index: "))
		key, value = input("Input field you want to edit and new value separated by space: ").split()
		edit(ind, key, value)

	@check_edit
	def edit(self, ind, key, value):
		setattr(self.adresses[ind], key, value) 

	def save_to_json(self, file_name):
		with open(file_name, 'w') as file:
			file.write("")
		with open(file_name, 'a') as file:
			for adr in self.adresses:
				file.write(json.dumps(adr.__dict__) + "\n")

	def find_adress(self, search_str):
		res = AdressList()
		for adr in self.adresses:
			for value in adr.__dict__.values():
				if search_str.lower() in str(value).lower():
					res.adresses.append(adr)
					break
		return res

	@check_parameter
	def sort(self, parameter):
		get_parameter = lambda adr: str(getattr(adr, parameter)).lower() if type(getattr(adr, parameter)) is str else getattr(adr, parameter)
		self.adresses.sort(key = get_parameter)

	def print(self):
		for x in self.adresses:
			x.print()
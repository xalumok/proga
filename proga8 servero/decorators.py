from copy import deepcopy
def check_adress(func):
	def wrapper(self, new_adr):
		try:
			if (new_adr.validate()):
				return func(self, new_adr)
			else:
				print("bad input")
		except:
			print('bad input')
	return wrapper

def check_edit(func):
	def wrapper(self, ind, key, value):
		try:
			assert hasattr(self.adresses[ind], key)
			new_adr = deepcopy(self.adresses[ind])
			setattr(new_adr, key, value)
			if new_adr.validate() == False:
				print("bad input")
			else:
				func(self, ind, key, value)
		except:
			print("bad input")
	return wrapper

def check_index(func):
	def wrapper(self, ind):
		if 0 <= ind < len(self.adresses):
			func(self, ind)
	return wrapper

def check_parameter(func):
	def wrapper(self, parameter):
		adr = Adress()
		if hasattr(adr, parameter):
			func(self, parameter)
	return wrapper

def check_add_info(func):
	def wrapper(self, info):
		if len(info) != len(list(Adress().__dict__.keys())):
			print("Bad input")
		else:
			func(self, info)
	return wrapper
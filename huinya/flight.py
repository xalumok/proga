import json
class Flight:
	def __init__(self):
		self.destination = ""
		self.departure = ""
		self.id = 0
		self.dates = list()

	def reader(self, input_dict, *kwargs):
		for key in input_dict:
			try:
				setattr(self, key, input_dict[key])
			except:
				print("Wrong input JSON")
				exit(0)

	def validate(self):
		if not self.departure.isalpha():
			return False
		if not self.destination.isalpha():
			return False
		try:
			self.id = int(self.id)
			if self.id <= 0:
				return False
		except:
			return False
		try:
			for date in self.dates:
				date = int(date)
				if date <= 0 or date > 31:
					return False
		except:
			return False

		return True

	def print(self):
		print(self.__dict__)


class FlightList:
	def __init__(self):
		self.flights = []

	def read_json(self, input_json):
		for x in input_json:
			flight = Flight()
			try:
				flight.reader(json.loads(x))
				if (flight.validate()):
					self.flights.append(flight)
				else:
					print("bad input")
			except:
				print('bad input')

	def add(self):
		print("Input values in this order", str(list(Flight().__dict__.keys())))
		info = input().split()
		if len(info) != len(list(Flight().__dict__.keys())) + 6:
			print("Bad info len(bad input)")
			return
		flight = Flight()
		ind = 0
		for key in flight.__dict__.keys():
			if (key != "dates"):
				setattr(flight, key, info[ind])
				ind += 1
		try:
			while ind < len(info):
				flight.dates.append(int(info[ind])) #Lviv Kyiv 23423 1 2 3 4 5 6 7
				ind += 1
		except:
			print("bad date input")
			return

		try:
			if (flight.validate()):
				self.flights.append(flight)
			else:
				print("bad input")
		except:
			print('bad input')

	def delete(self, ind):
		if ind >= 0 and ind < len(self.flights):
			del self.flights[ind]
		else:
			print("invalid index")

	def edit(self):
		try:
			ind = int(input("Input index: "))
			key, value = input("Input field you want to edit and new value separated by space: ").split()
			if not hasattr(self.flights[ind], key):
				print("bad key input")
				return
			old_value = getattr(self.flights[ind], key)
			setattr(self.flights[ind], key, value) 
			if self.flights[ind].validate() == False:
				print("bad input(validate failed)")
				setattr(self.flights[ind], key, old_value) 
		except:
			print("bad input")

	def save_to_json(self, file_name):
		with open(file_name, 'w') as file:
			file.write("")
		with open(file_name, 'a') as file:
			for flight in self.flights:
				file.write(json.dumps(flight.__dict__) + "\n")

	def find_flight(self, search_str):
		res = FlightList()
		for flight in self.flights:
			for value in flight.__dict__.values():
				if search_str.lower() in str(value).lower():
					res.flights.append(flight)
		return res

	def sort(self, parameter):
		try:
			get_parameter = lambda flight: str(getattr(flight, parameter)).lower()
			self.flights.sort(key = get_parameter)
		except:
			print("bad sort parameter")

	def print(self):
		for x in self.flights:
			x.print()
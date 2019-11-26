import datetime

class Date:
	def __init__(self, day = 23, month = 10, year = 2019):
		self.day = day
		self.month = month
		self.year = year
	def isOk(self):
		isOk = True
		try:
			datetime.datetime(self.year, self.month, self.day)
		except ValueError:
			isOk = False
		return isOk
		

	def __str__(self):
		res = ""
		res += str(self.year) + "-"
		if (self.month < 10):
			res += "0" + str(self.month)
		else:
			res += str(self.month)
		res += "-"
		if (self.day < 10):
			res += "0" + str(self.day)
		else:
			res += str(self.day)
		return res

	def __lt__(self, other):
		return str(self) < str(other)
	def __gt__(self, other):
		return str(self) > str(other)
	def __le__(self, other):
		return str(self) <= str(other)
	def __ge__(self, other):
		return str(self) >= str(other)

	def daysTo(self, other):
		cur = datetime.datetime(self.year, self.month, self.day)
		endD = datetime.datetime(other.year, other.month, other.day)
		return int((endD - cur).days) + 1




class Booking:
	def __init__(self, name = "", price = 0.0, startDate = Date(), endDate = Date()):
		self.name = name
		self.price = price
		self.startDate = startDate
		self.endDate = endDate

	def getWholePrice(self):
		return self.price * self.startDate.daysTo(self.endDate)



class Bookings:
	def __init__(self, fileName):
		self.arr = []
		with open(fileName) as f:
			lines = f.readlines()
		for line in lines:
			info = line.split()
			try:
				cur_book = Booking(info[0], float(info[1]), Date(int(info[2]), int(info[3]), int(info[4])), Date(int(info[5]), int(info[6]), int(info[7])))
				self.add(cur_book)
			except:
				print("Bad booking data")
			

	def intersects(self, booking):
		for cur in self.arr:
			if not(booking.startDate > cur.endDate or booking.endDate < cur.startDate):
				return True
		return False


	def add(self, booking):
		if (len(self.arr) % 2 == 1):
			booking.price += 10
		if (self.intersects(booking)):	
			print("{} is intersecting existing bookings so it won't be added".format(booking.name))
		elif booking.price < 0:
			print("bad booking price")
		elif booking.name.isalpha() == False:
			print("Bad booking name")
		elif booking.startDate > booking.endDate:
			print("Start date is less than end date")
		elif booking.startDate < Date(23, 10, 2019):
			print("Start date is less than 23-10-2019")
		elif booking.startDate.isOk() == False or booking.endDate.isOk() == False:
			print("Bad booking date")
		else:
			self.arr.append(booking)
			print("added successfully")

	def printAll(self):
		for booking in self.arr:
			print("{", booking.name, booking.price, booking.startDate, booking.endDate, "}, totalPrice =", booking.getWholePrice())



print("Adding from file...")
b = Bookings("input.txt")

while True:
	print()
	print("1 - Print bookings")
	print("2 - Add a booking")

	pick = int(input())

	if pick == 1:
		b.printAll()
	else:
		print("Input [name] [pricePerDay] [dayStart] [monthStart] [yearStart] [dayEnd] [monthEnd] [yearEnd]")
		info = input().split()
		cur_book = Booking(info[0], float(info[1]), Date(int(info[2]), int(info[3]), int(info[4])), Date(int(info[5]), int(info[6]), int(info[7])))
		b.add(cur_book)

b.printAll()

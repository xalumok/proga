class Date:
  def __init__(self, day, month, year):
    self.day = day
    self.month = month
    self.year = year

  def getDay(self):
    return self.day

  def getMonth(self):
    return self.month

  def getYear(self):
    return self.year

  def setDay(self, day):
    if day < 1 and day > 31:
      print("wrong input!")
    else:
      self.day = day

  def setMonth(self, month):
    if month < 1 and month > 12:
      print("wrong input!")
    else:
      self.month = month

  def setYear(self, year):
    if year < 2019:
      print("wrong input!")
    else:
      self.year = year

#27 10 2019 - 10 11 2019     12

class Booking:
  def __init__(self, name, pricePerDay, startDate, endDate):
    self.name = name
    self.pricePerDay = pricePerDay
    self.startDate = startDate
    self.endDate = startDate

  def output(self):
    print("name: ", self.name, ", price: " , self.pricePerDay, ", startDate", self.startDate.getDay(), self.startDate.getMonth(),self.startDate.getYear(), ", endDate: ", self.endDate.getDay(), self.endDate.getMonth(), self.endDate.getYear())

bookings = []
file = open('right.txt', 'r')
for line in file.readlines():
    row = list(line.split())
    start = Date(int(row[2]), int(row[3]), int(row[4]))
    end = Date(int(row[5]), int(row[6]), int(row[7]))
    booking = Booking(row[0], int(row[1]), start, end)
    bookings.append(booking)

for booking in bookings:
  booking.output()

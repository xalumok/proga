from pickle import *

class Ameba:
	def __init__(self):
		self.aa = True
		self.name = "AMB"

amb = Ameba()

bt = dumps(amb)

amb1 = loads(bt)
print(amb1.name)
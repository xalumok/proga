import json
from adress import *
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

pole = "surname"

setattr(adresses[0], pole, "Max")
for x in adresses:
	x.print()
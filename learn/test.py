import json

class Country:
    def init(self):
        self.name = ""
        self.square = 0
        self.amount = 0

    def read(self, input_dict, *kwargs):
        for key in input_dict:
            try:
                setattr(self, key, input_dict[key])
            except:
                print("Wrong input JSON")
                exit(0)

    def print(self):
        print("Country{ Country: ", self.name , "Square: ", self.square, "Amount: ", self.amount, "}" )

def sort_by_name(country_list):
    get_name = lambda country: country.name
    country_list.sort(key = get_name)

def sort_by_square(country_list):
    get_square = lambda country: country.square
    country_list.sort(key = get_square)

def sort_by_amount(country_list):
    get_amount = lambda country: country.amount
    country_list.sort(key = get_amount)

def find_by_name(country_list, search_name):
    for country in country_list:
        if country.name == search_name:
            return country
    return None

with open("textfile.json", 'r') as file:
    input_json = file.readlines()

countries = []

for i in input_json:
    current_country = Country()
    current_country.read(json.loads(i))
    countries.append(current_country)

for i in countries:
    i.print()

while True:
    print("Choose the option: ")
    print(" 1. Sort by name")
    print(" 2. Sort by square")
    print(" 3. Sort by amount")
    print(" 4. Find by name")

    x = input()
    if x == "":
        continue
    x = int(x)
    if( x>4 or x<1):
      print("There is no such option!")  
      continue
    if x == 1:
        sort_by_name(countries)
    if x == 2:
        sort_by_square(countries)
    if x == 3:
        sort_by_amount(countries)
    if x == 4:
        print("Input Country Name: ")
        name = input()
        if find_by_name(countries, name) != None:
        	find_by_name(countries, name).print()
        else:
        	print("No country found")
    if x != 4:
        for x in countries:
            x.print()
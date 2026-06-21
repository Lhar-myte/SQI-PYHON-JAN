yoruba_translator = {"head": "ori", "shoe": "bata", "air": "afefe"}
print(yoruba_translator)
yoruba_translator["snake"] = "ejo"
print(yoruba_translator)
del yoruba_translator["head"]
print(yoruba_translator)


# car = {"brand": "toyota", "year": 2017, "colour": "black"}
# print(car)
# nums_animal_legs = {"lion": 4, "duck": 2, "snake": 0}
# nums_animal_legs["hen"] = 2
# nums_animal_legs["snake"] = 100
# del nums_animal_legs["lion"]
# print(nums_animal_legs)

employees = {
    "Lusi": "CEO",
    "Adeoye": "Chairman",
    "Mrs. Akintola": "Human Resources",
    "Roqeeb": "Head of IT",
    "Timothy": "Human Resources"
}
print(employees.get("Lusi"))
print(employees.get("adeoye", "Not in the dictionary"))

print(employees["Lusi"])
# employees["adeoye", "Not in the dictionary"]
print(employees.setdefault("winnie", "CER"))

my_car = {"brand": "bradbus_benz", "electric": True, "year": 2026, "colours": ["Black", "Brown", "Red"]}
brand = my_car["brand"]
is_electric = my_car["electric"]
Year_manufacture = my_car["year"]
colours = my_car["colours"]

print(brand = my_car["brand"])
print(is_electric = my_car["electric"])
print(Year_manufacture = my_car["year"])
print(colours = my_car["colours"])
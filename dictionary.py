cars={"toyota": "camry",
      "mahindra": "xuv",
      "honda":"crv",
      "hyundai":"verna"}
print(cars)
# print(dir(cars))
# print(help(cars))
print(cars.get("honda"))

if cars.get("hyundai"):
    print("the brand is there")
else:
    print("the brand does not exsist")
print(type(cars))

cars.update({"bmw":"x5"})
print(cars)

cars.update({"honda":"city"})
print(cars)

cars.pop("hyundai")
print(cars)

cars.popitem()
print(cars)

keys=cars.keys()
print(keys)

value=cars.values()
print(value)
for keys in cars.keys():
    print(keys)
for value in cars.values():
    print(value)
item = cars.items()
print(item)

for key, value in cars.items():
     print(f"{key} : {value}")
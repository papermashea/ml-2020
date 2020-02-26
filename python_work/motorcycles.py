motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
motorcycles[0] = 'triumph'
# print(motorcycles)
motorcycles.append('bmw')
# print(motorcycles)		
# del motorcycles[2]
print(motorcycles)

# popped_motorcycles = motorcycles.pop()
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.upper() + ".")
# print(popped_motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
motorcycles.append('bmw')
print(motorcycles)
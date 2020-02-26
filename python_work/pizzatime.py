requested_toppings = ['mushrooms', 'anchovies', 'peppers', 'onions']
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		# if 'mushrooms' in requested_toppings:
		# 	print("Adding mushrooms...")
		# if 'peppers' in requested_toppings:
		# 	print("Adding peppers...")
		# if 'anchovies' in requested_toppings:
		# 	print("Are you sure about the anchovies?")
		if requested_topping == 'onions':
			print("Sorry, we are out of onions right now :(")
		else:
			print("Adding " + requested_topping + " to your pie!")

	print("\nFinished making your pizza!")

else:
 print("Are you sure you want a nothing pizza?")

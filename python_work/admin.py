users = ['megan', 'katie', 'bill', 'tom', 'admin']
# users = []

# if users:
# 	for user in users:
# 		if user is 'admin':
# 			print("Welcome,admin! Time to get to work.")
# 		else:
# 			print("What would you like to do today?")
# else:
# 	print("We need to find some users!")

current_users = ['phil', 'bob', 'mat', 'tom', 'QUINN']
new_users = ['ry', 'bri', 'connor', 'liam', 'brigid', 'quinn', 'mat']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
	if new_user in current_users.lower():
		print("Please pick a new username.")

	elif new_user in current_users.upper():
		print("Please pick a new username.")

	# elif new_user in current_users:	
	# 	print("Please pick a new username.")
	else:
		print("Ok " + new_user.title() + ", let's set up your account")


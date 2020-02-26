guest_list = ['val', 'erica', 'jon', 'bailey']
# print(guest_list)

# guest_list.append('rhiannon')
# guest_list.remove('jon')

guest_list.append('rhiannon')
guest_list.remove('jon')

invite1 = "hey " + guest_list[0] + " come to dinner party part II next weekend at 5!"
invite2 = "hey " + guest_list[1] + " come to dinner party part II next weekend at 5!"
invite3 = "hey " + guest_list[2] + " come to dinner party part II next weekend at 5!"
invite4 = "hey " + guest_list[3] + " come to dinner party part II next weekend at 5!"

# print(invite1)
# print(invite2)
# print(invite3)
# print(invite4)

# guest_list.append('rhiannon')
# guest_list.remove('jon')

print(guest_list)
print(invite1)
print(invite2)
print(invite3)
print(invite4)

table1 = "actually i can't cook, sorry " + guest_list[2]
table2 = "actually i can't cook, sorry " + guest_list[3]

print(table1)
print(table2)

pop_invite1 = "come over for ramen at 7 " + guest_list.pop(0)
pop_invite2 = "come over for ramen at 7 " + guest_list.pop(0)

print (pop_invite1)
print (pop_invite2)

del guest_list[0]
del guest_list[0]

print(guest_list)
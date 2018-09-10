grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

#print('First Item', grocery_list[0])

#print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids']
to_do_list = [grocery_list, other_events]

print(to_do_list)

grocery_list.append('Onions')

print(to_do_list)


grocery_list.insert(1, 'Pickle')

print(to_do_list)

grocery_list.remove('Pickle')

grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))

print(max(to_do_list2))

print(min(to_do_list2))
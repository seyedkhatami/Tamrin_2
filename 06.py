my_list = [1, 2, 3, 4]

print(my_list)

my_list.append(2)

print(my_list)

print("...............")

new_list = [1, 2, 3, 4]
old_list =  []

old_list.extend(new_list)
old_list.append(2)

print(new_list)
print(old_list)
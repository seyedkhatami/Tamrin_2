user_inpt_you = input()
box = user_inpt_you.split()
for index, item in enumerate(box):
    user, inpt, you = box[0], box[1], box[2]

key = you.split()
for index, elem in enumerate(key):
    key[index] = int(elem)

print(f"{user}/{inpt}/{you}")

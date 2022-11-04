items1 = input().split("*")
items2 = input().split("*")

for index, item in enumerate(items2):
    items1.append(items2[index])

print(items1)

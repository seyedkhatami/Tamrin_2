user = input().split()

print(f"max :{max(user)}")
print("--------")
print(f"min :{min(user)}")
print(("--------"))

for index, item in enumerate(user):
    user[index] = int(item)

print(f"sum :{sum(user)}")
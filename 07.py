user = input().split()

for index, elem in enumerate(user):
    print

print(f"first word : {user.pop(0)}")
new_user = user.pop()
print(f"last word : {new_user}")

print(user)

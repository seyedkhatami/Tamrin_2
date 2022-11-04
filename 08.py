numbers = input().split()
x = 0
for index, elem in enumerate(numbers):
    numbers[index] = int(elem)

for num in numbers:
    x += int(num)

print(x)

numbers = set()
for num in range(10, 10 ** 6):
    if num == sum([int(i) ** 5 for i in str(num)]):
        numbers.add(num)
print(numbers)
print(sum(numbers))

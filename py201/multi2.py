numbers = [1, 2, 3, 4, 5]
factor = 5
numbers2 = []
for num in numbers:
    product = num * factor
    numbers2.append(product)
print numbers2
numbers3 = [1, 2, 3, 4, 5]
numbers4 = [2, 4, 6, 8, 10]
results = []
for num3 in numbers3:
    for num4 in numbers4:
        results.append(num3 * num4)
print results
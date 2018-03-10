def positive(numbers):
    for num in numbers:
        if num >= 0:
            print num
    positive = []
    for num in numbers:
        if num >= 0:
            positive.append(num)
    print positive
numbers = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]
positive(numbers)
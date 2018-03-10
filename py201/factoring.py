def factoring(number):
    factors = []
    numberRange = range(1, number + 1)
    for num1 in numberRange:
        check = float(number) / float(num1)
        for num2 in numberRange:
            if check == num2:
                factors.append(check)
    for factPrint in factors:
        print int(factPrint)
    print factors
number = int(raw_input('Enter the number: '))
factoring(number)
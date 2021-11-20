def fib(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)

def getFibList(number):
    fib_list = []
    key = 1
    while (key < number + 1):
        fib_list.append(fib(key))
        key += 1
    return fib_list

print(getFibList(10))
print(getFibList(7))
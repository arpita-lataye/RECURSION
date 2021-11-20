def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3

index=1
while(index<10):
    print(pattern(index))
    index+=1
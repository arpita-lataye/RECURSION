def twopowers(number):
    if number==1:
        return 1
    return 2 * twopowers(number-1)

index=1
while(index<10):
    print(twopowers(index))
    index+=1

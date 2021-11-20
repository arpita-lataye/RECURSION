def power(x,y):
    if y==0:
        return 1
    else:
        return (x*power (x,y-1))
x=int(input('enter base:'))
y=int(input('enter exponent:'))
z=power(x, y)
print('calculated value=',z)
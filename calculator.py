import math

def factorial(number):
    ans = 1
    for i in range(2,number+1):
        ans = i*ans
    return ans

def power(base,exponent):
    return math.pow(base,exponent)

def squareroot(number):
    return math.sqrt(number)

def naturallog(number):
    return math.log(number)


print('Welcome User')
print('Select the option')



while True:
    print('-----------------********----------------')
    print('1.Square root\n2.factorial\n3.log\n4.power\n5.exit')
    inputnumber = int(input())
    if inputnumber == 5:
        break
    if inputnumber == 1:
        print('enter number')
        no = float(input())
        print('square root of given no is {0}'.format(squareroot(no)))
    elif inputnumber == 2:
        print('enter the no to find factorial')
        #check if no else error
        i = int(input())
        print('factorial for given no is {0}'.format(factorial(i)))
    elif inputnumber == 3:
        print('enter the no to find log')
        no = float(input())
        print('log of given no is {0}'.format(naturallog(no)))
    elif inputnumber == 4:
        print('enter base')
        base = float(input())
        print('enter exponent')
        exponent = float(input())
        print('base to the power exponent with given values is {0}'.format(power(base,exponent)))
    else:
        print('please select proper option')
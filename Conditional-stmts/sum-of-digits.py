#program to calculate the sum of digits

def SumOfDigits(n):

    if n == 0:
        return 0

    return n % 10 + SumOfDigits(n//10)

num =int(input())

SumOfDigits(num)

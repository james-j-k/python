#program to check whether the number input is
#positive, negative, odd, even or zero

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")

    if num % 2 == 0:
        print("Even")
    
    else:
        print("Odd")

elif num < 0:
    print("Negative")

else:
    print("Zero")


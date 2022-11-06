def whichIsGreater(num1, num2):
    #start here
    if num1 > num2:
        num = 1
    else:
        num = 0

    return num

num1, num2 = input().split()
print(whichIsGreater(num1, num2))
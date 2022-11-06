def reverseBinary(num):
    revs_number = 0

    if num >= 1 and num <= 1000000000:
        reversed = int(bin(num)[:1:-1], 2)
        
    else:
        reversed = "Error"

    return reversed

num = int(input())
print(reverseBinary(num))
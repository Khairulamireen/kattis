num = int(input())

if num >= 1 and num <=100:
    for n in range (num):
        num = n + 1
        print(str(num) + " Abracadabra")
else:
    print("error")

import math
n = int(input())
m = int(input())

for i in range(n):
    a = math.ceil(n%m)
    for j in range(a):
        print("*", end="")
    m = m - a
    print()

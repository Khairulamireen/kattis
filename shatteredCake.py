w = int(input())
n = int(input())
total= 0

for i in range (n):
    m, k = map(int, input().split())
    size = m * k
    total = total + size

l = int(total/w)
print(l)
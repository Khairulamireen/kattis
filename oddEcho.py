n = int(input())
m = []

for i in range (n):
    m.append(str(input()))

for j in range (len(m)):
    a = int(j%2)
    if a == 0:
        print(m[j])


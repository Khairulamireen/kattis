a, b=0, ' '
i, j = 5, 1

for k in range (i, -1, -1):
    print((k*b)+(j*str(a)))
    a = a+1
    j = j+1

a=0
i, m = 5, 1

for k in range (0,i):
    print((m*str(a)))
    a = a+1
    m = m+1

a, b=0, ' '
i, j = 5, 1

for k in range (i, -1, -1):
    print((k*b)+(j*str(a)*2))
    a = a+1
    j = j+1

n =5
for h in range(0,n):
    print(str(h)*(h+1))
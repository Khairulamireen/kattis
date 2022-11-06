import math
n = int(input())

for i in range (n):
    line = input().strip()
    size = int(math.sqrt(len(line)))
    m = []
    for j in range(size):
        m.append([])
    for idx, c in enumerate(line):
        m[int(idx / size)].append(c)
    
    rotated = list(zip(*(m)))[::-1]
    print(''.join([c for l in rotated for c in l]))
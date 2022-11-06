def areaTriangle(height, base):
    #area of triangle
    area = float((0.5*height)*base)
    return area


height, base = input().split()
height, base = float(height), float(base)
print(areaTriangle(height, base))
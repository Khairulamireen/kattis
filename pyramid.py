# for i in range(0, 5):
#     for j in range(0, i+1):
#         print("* ", end="")
#     print()

# # for i in range (0, 5):
# #     for j in range(0, i+1):
# #         print(i, end="")
# #     print()

# a = 8

# for i in range(0,5):        # num of rows
#     for j in range(0, a):   # num of columns
#         print(end=' ')
#     a = a - 2
#     for j in range(0, i+1):
#         print("* ", end="")
#     print()

n = 5

for i in range (n):
    print(" "*(n-i-1), end="")
    for j in range(i+1):
        print(i+1, "", end="")
    print()
"""
1
0 1
1 0 1
"""

## Code

n = int(input("Enter the no. of Lines: "))
for i in range(n):
    for j in range(i+1):
        if i%2 == 0:
            if j%2 == 0:
                print(1, end = " ")
            else:
                print(0, end = " ")
        else:
            if j%2 != 0:
                print(1, end = " ")
            else:
                print(0, end = " ")
    print()
pass

## Optimized Code

n = int(input("Enter the no. of Lines: "))
for i in range(n):
    for j in range(i+1):
        print((i + j + 1) % 2, end=" ")
    print()

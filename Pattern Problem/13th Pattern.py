"""
1
2 3
4 5 6
"""

## Code

n = int(input("Enter the no. of Lines: "))
k = 1
for i in range(n):
    for j in range(i+1):
        print(k, end = " ")
        k += 1
    print()
pass
"""
1         1
1 2     2 1
1 2 3 3 2 1
"""

## Code

n = int(input("Enter the no. of Lines: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end = " ")
    for j in range(2*(n-i-1)):
        print("*", end = " ")
    for j in range(i+1,0,-1):
        print(i+1, end = " ")
    print()
pass
"""
1
2 2
3 3 3
4 4 4 4
"""

## Code

n = int(input("Enter the number of Lines: "))
for i in range(n):
    for j in range(i+1):
        print(i+1, end = " ")
    print()
pass
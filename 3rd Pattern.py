"""
1 
1 2 
1 2 3 
"""

## Code

n = int(input("Enter the No. of Lines: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end = " ")
    print()
pass
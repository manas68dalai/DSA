"""
C
C B 
C B A
"""

## Code

n = int(input("Enter the no. of Lines: "))
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-j-1), end = " ")
    print()
pass
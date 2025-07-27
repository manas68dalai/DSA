"""
A B C
A B
A
"""

## Code

n = int(input("Enter the no. of Lines: "))
ascii_val = 65
for i in range(n):
    for j in range(n-i):
        print(chr(ascii_val+j), end = " ")
    print()
pass
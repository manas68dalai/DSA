"""
A
A B
A B C
"""

## Code

n = int(input("Enter the no. of Lines: "))
ascii_val = 65
for i in range(n):
    for j in range(i+1):
        print(chr(ascii_val+j), end = " ")
    print()
pass
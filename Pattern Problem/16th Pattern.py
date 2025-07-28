"""
A
B B
C C C
"""

## Code

n = int(input("Enter the no. of Lines: "))
ascii_value = 65
for i in range(n):
    for j in range(i+1):
        print(chr(ascii_value + i), end = " ")
    print()
pass
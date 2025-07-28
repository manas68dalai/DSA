"""
    A
  A B A
A B C B A
"""

## Code

n = int(input("Enter the no. of Lines: "))
ascii_val = 65
for i in range(n):
    for j in range(n-i-1):
        print(" ", end =" ")
    for j in range(i+1):
        print(chr(ascii_val + j), end = " ")
    for j in range(i-1,-1,-1):
        print(chr(ascii_val+j), end = " ")
    print()
pass
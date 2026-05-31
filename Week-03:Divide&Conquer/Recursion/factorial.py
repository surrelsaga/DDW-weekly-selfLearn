# Pseudocode
# Input: n, an integer
# Output: factorial of n, an integer
# Steps:
# 1. if n is equal to 0 or to 1
#     1.1 return 1
# 2. otherwise,
#     2.1 return n x factorial of n-1

number = 10

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * calculate_factorial(n - 1)

print( calculate_factorial(number) )

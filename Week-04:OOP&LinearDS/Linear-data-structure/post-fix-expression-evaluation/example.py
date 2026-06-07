# Using stack data structure to evaluate a mathematical expression

# Infix notation: 3 + 4 x 2
# => can rewrite in POST-FIX notation (operands are placed before the operators): 4 2 x 3 +

# We will implement this using stack

# Steps to implement:
# Post-Fix Evaluation Steps:
# 1. Read the expression from left to right.
# 2. If it is an operand (not an operator symbol), do the following:
#     2.1. put the operand into the stack.
# 3. Otherwise (this is an operator), do the following:
#     3.1. pop out the top of the stack as the *right* operand
#     3.2. pop out the top of the stack as the *left* operand
#     3.3. evaluate the operator with the operands
#     3.4. push the result into the stack

# Stack will be a class (Last in First out)
# Stack
# Attributes:
# 1. items

# Methods:
# 1. Push // insert
# 2. Pop // remove and read
# 3. Peek // only read

class Stack:
    # attributes
    def __init__(self):
        self._items = []
        
    # method getter for item list
    @property
    def items(self):
        return self._items
    
    # basic methods of a stack
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        self.items.pop()
        
    def peek(self):
        return self.items[-1]

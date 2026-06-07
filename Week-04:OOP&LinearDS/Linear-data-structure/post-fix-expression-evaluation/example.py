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
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]

# Main function to evaluate a post fix expression
def evaluate_postfix(expression):
    operandStack = Stack()
    
    # Separate characters inside the string
    # we gather them in a list
    chars = expression.split(' ')
    
    for char in chars:
        # if a character is an operand (a digit)
        if char.isnumeric() == True:
            # convert to number type first because after split, the digit is a str
            char = int(char)
            operandStack.push(char)
        # if it's an operator (+, -, :, x)
        else:
            right_operand = operandStack.pop()
            left_operand = operandStack.pop()
            
            if char == '+':
                result = left_operand + right_operand
            elif char == '-':
                result = left_operand - right_operand
            elif char == '*':
                result = left_operand * right_operand
            elif char == '/':
                result = left_operand / right_operand
                
            operandStack.push(result)
                
    # when the loop is over, the final number will be the result of the expression
    return operandStack.pop()

expression = "4 2 / 3 +"

print( evaluate_postfix(expression) )
                
            
            

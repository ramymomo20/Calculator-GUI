import math, re
from functools import reduce

#*-------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({self.value})"

    __repr__ = __str__

#*-------------------------------------------------------------------------------------------------
class Stack:
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{self.top}\nStack:\n{out}')

    __repr__=__str__


    def isEmpty(self):
        return self.top == None # Validate whether stack is empty or not.

    def __len__(self):
        count = 0 # Count the number of elements in the stack.
        current = self.top

        while current is not None: 
            current = current.next # Set the current node as the next node in the stack. 
            count += 1
        return count

    def push(self,value): 
        node = Node(value) # Adds an element on top of stack.
        node.next = self.top
        self.top = node # Sets the top of the stack as node value.

     
    def pop(self): 
        if not self.isEmpty(): # Removes an element from stack. Validate isEmpty. 
            temp = self.top.value # Store value temporarily to be returned.
            self.top = self.top.next # Assign the pointer to the next Node.
            return temp
        else:
            return None

        
    def peek(self): 
        if not self.isEmpty(): # Returns the top element of the stack without removing it.
            return self.top.value
        else:
            return None

#*-------------------------------------------------------------------------------------------------
class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr = new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        try:
            float(txt)
            return True
        except ValueError: # When there is a ValueError, return false.
            return False


    def _getPostfix(self, txt):
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression

        operators = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3} # Using dictionary keys to prioritize order of operations, from 3 -> 1.
        (open_parenthesis_count, closed_parenthesis_count, numbers_count, operator_count) = (0, 0, 0, 0) # Initialize the counts for operators, numbers, and open/close parenthesis.

        postfix = '' # postfix is going to output as a string.
        equation = [] # Insert the contents of txt into a list for better manipulation and as a mutable data type.

        for contents in txt.split(): # Take the contents in txt and split them all into a list.
            equation.append(contents)

        length = len(equation) # Count the number of elements in the list.

        for tokens in range(0, length):
            if equation[tokens] in operators.keys(): # Counts the number of operators in the equation list.
                operator_count += 1
                if equation[tokens] not in operators.keys(): # Check if there are no operators in the equation.
                    return None
            else:
                pass
            
            if self._isNumber(equation[tokens]): # Count the amount of numbers in the expression.
                numbers_count += 1

            elif equation[tokens] == '(' and equation[tokens] == ')': # Count the number of open and closed parenthesis.
                open_parenthesis_count += 1
                closed_parenthesis_count += 1
            else: # Else, count them separately.
                if equation[tokens] == '(':
                    open_parenthesis_count += 1
                else:
                    if equation[tokens] == ')':
                        closed_parenthesis_count += 1
        
        if (numbers_count == operator_count + 1) and (open_parenthesis_count == closed_parenthesis_count): # Validate that there are no unbalanced parenthesis or more operators than numbers.
            for contents in txt.split():
                if not self._isNumber(contents) and contents != "(" and contents != ")": # If not a number nor contain ( and ), then check for other operators.
                    if postfixStack.peek() == "^" and contents == "^" and not postfixStack.isEmpty(): # If ^ is in the stack and in contents, push it to the top of the stack.
                        postfixStack.push(contents)
                    else:
                        while not postfixStack.isEmpty() and postfixStack.peek() != "(" and operators[contents] <= operators[postfixStack.peek()]: # Check if the stack isn't empty and that the top isn't an open parenthesis.
                            postfix = postfix + str(postfixStack.pop()) + " " # Create the postfix by adding the stack nodes.
                        else:
                            postfixStack.push(contents) # If none of the conditions are met, push contents to top of stack.
                else:
                    if self._isNumber(contents):
                        postfix = postfix + str(float(contents)) + " "

                    if contents == "(" and contents == ")": # If the token is a parenthesis, push that to the stack.
                        postfixStack.push(contents)
                        if postfixStack.peek() != "(" and not postfixStack.isEmpty():
                            postfix = postfix + str(postfixStack.pop()) + " "
                        else:
                            postfixStack.pop() # Removes the top node in the stack.

                    elif contents == "(" and contents != ')': # Search for any open parenthesis and count the closed ones too.
                        postfixStack.push(contents)
                    elif contents == ')' and contents != '(':
                        while postfixStack.peek() != "(" and not postfixStack.isEmpty():
                            postfix = postfix + str(postfixStack.pop()) + " "
                        else:
                            postfixStack.pop()

        else: # If neither condition is followed, return None.
            return None
                        
        while not postfixStack.isEmpty(): # Check if the stack isn't empty.
            if postfixStack.peek() not in "(": # If the top node doesn't have a open parenthesis.
                postfix = postfix + str(postfixStack.pop()) + " "
            else:
                return None

        return postfix[:-1] # Remove the space at the end of the postfix.


    @property
    def calculate(self):
        if not isinstance(self.__expr,str) or len(self.__expr) <= 0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the expression
        postfix = self._getPostfix(self.__expr) # Receives the postfix expression.

        if postfix != None: # Validates postfix expression.
            for operator in postfix.split(): # Iterate through the expression.
                if not self._isNumber(operator): 
                    (second_number, first_number) = (calcStack.pop(), calcStack.pop()) # Set the first number and second number equal to the calcStack.pop().                    
                    if operator == '^': # Exponents
                        calcStack.push(float(first_number) ** float(second_number))

                    if operator == '*': # Multiplication
                        calcStack.push(float(first_number) * float(second_number))

                    if operator == '/': # Division
                        if second_number != 0: # Validate any divide by 0 case.
                            calcStack.push(float(first_number) / float(second_number))
                        else:
                            return 'Error'
                    if operator == '+': # Addition
                        calcStack.push(float(first_number) + float(second_number)) # Doesn't matter the order of addition, due to the commutative property.

                    if operator == '-': # Subtraction
                        calcStack.push(float(first_number) - float(second_number))
                else:
                    calcStack.push(float(operator)) # If neither operator is found in the expression, push the number onto the stack.
        else:
            return None
        
        y = calcStack.pop()

        return int(y) if y - int(y) == 0 else str(round(y,4)) # After the calculations are calculated, pop the final value from the stack and return it.

#*-------------------------------------------------------------------------------------------------
def factorial_parser(txt):
    x = re.split("([()+-/*!])", txt.replace(" ", ""))

    values = [x[i-1] for i in [i for i in range(len(x)) if x[i] == '!']] # Gives you the number that is due for the factorial by finding each index '!' appears.
    fact_values = [str(math.factorial(i)) for i in map(int, values)] # Calculates the factorial for each number.

    myDict = dict(zip([i + ' !' for i in values], fact_values)) # Compares the original string representation with its factorial value.
    
    return reduce(lambda a, kv: a.replace(*kv), myDict.items(), txt) # Replaces all factorial instances in string with its factorial in-place.
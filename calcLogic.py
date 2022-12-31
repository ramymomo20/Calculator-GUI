import functools

#*-------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

#*-------------------------------------------------------------------------------------------------
class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def __len__(self):
        count = 0
        current = self.top

        while current is not None: 
            current = current.next 
            count += 1
        return count

    def push(self,value): 
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.isEmpty():
            temp = self.top.value
            self.top = self.top.next
            return temp
        else:
            return None

    def peek(self):
        return self.top.value if not self.isEmpty() else None

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
        except ValueError:
            return False

    def _getPostfix(self, txt):
        stack = []
        operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "!": 4, "(": 0}
        postfix = []

        i = 0
        while i < len(txt):
            if txt[i].isspace():
                i += 1
            elif txt[i].isdigit():
                start = i
                while i < len(txt) and txt[i].isdigit():
                    i += 1
                postfix.append(txt[start:i])
            elif txt[i] in operators:
                token = txt[i]
                if token == "!" and (i == 0 or txt[i-1] == " "):
                    postfix.append(token)
                else:
                    while stack and operators[token] <= operators[stack[-1]]:
                        postfix.append(stack.pop())
                    stack.append(token)
                i += 1
            elif txt[i] == "(":
                stack.append(txt[i])
                i += 1
            elif txt[i] == ")":
                while stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
                i += 1
            else:
                raise ValueError(f"Invalid token: {txt[i]}")

        while stack:
            postfix.append(stack.pop())

        return " ".join(postfix)

    @property
    def calculate(self):
        @functools.lru_cache(maxsize=None)
        def factorial(x):
            if x == 0:
                return 1
            else:
                return x * factorial(x-1)

        stack = Stack()

        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "^": lambda x, y: x ** y,
            "!": factorial
        }
        postfix = self._getPostfix(self.__expr)

        for token in postfix.split():
            if token.isdigit():
                stack.push(float(token))

            elif token == "!":
                x = stack.pop()
                stack.push(operators[token](x))

            elif token in operators:
                y = stack.pop()
                x = stack.pop()
                stack.push(operators[token](x, y))
            else:
                return None

        ans = stack.pop()
        return int(ans) if ans - int(ans) == 0 else str(round(ans,4))
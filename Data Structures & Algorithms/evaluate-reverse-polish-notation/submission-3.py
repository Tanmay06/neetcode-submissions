class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        express = ""
        operators = {'+' : self.add, '-' : self.sub, '*' : self.mul, '/' : self.div}

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                express += '(' + str(a) + token + str(b) + ')'
                stack.append(operators[token](a,b))
            else:
                stack.append(int(token))
        
        return stack[0]
    


    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return int(a / b)
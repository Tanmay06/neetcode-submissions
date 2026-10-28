class MinStack:

    # def __init__(self):
    #     self.stack = []
    #     self.minstack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     val = min(val, self.minstack[-1] if self.minstack else val)
    #     self.minstack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minstack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minstack[-1]

# Time O(1)
# Sace O(n)

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        encoded = self.stack.pop()
        if encoded < 0:
            self.min = self.min - encoded

    def top(self) -> int:
        encoded = self.stack[-1]
        if encoded > 0:
            return encoded + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

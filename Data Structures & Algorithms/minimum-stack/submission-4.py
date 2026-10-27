class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = self.min if self.min < val else val

    def pop(self) -> None:
        if self.min == self.stack.pop():
            self.min = sorted(self.stack)[0] if self.stack else float('inf')
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Time O(nlogn)
# Space O(n)
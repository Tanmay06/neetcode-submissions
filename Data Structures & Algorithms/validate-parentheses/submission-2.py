class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { '(':')', '{':'}', '[':']'}
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if c == stack[-1]:
                        stack.pop()
                    else:
                        return False
        
        return len(stack) == 0

        # Time O(n)
        # Space O(n)
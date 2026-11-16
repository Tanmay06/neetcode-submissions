class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        print(filtered)
        i = 0
        j = len(filtered) - 1

        while i <= j:
            if filtered[i] != filtered[j]:
                return False
            i += 1
            j -= 1
        
        return True
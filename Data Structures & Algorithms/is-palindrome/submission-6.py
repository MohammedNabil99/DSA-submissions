class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        leftPtr = 0
        rightPtr = len(s) - 1
        
        while leftPtr < rightPtr:
            if not s[leftPtr].isalnum():
                leftPtr += 1
            elif not s[rightPtr].isalnum():
                rightPtr -= 1
            else:
                if s[leftPtr].lower() == s[rightPtr].lower():
                    leftPtr += 1
                    rightPtr -= 1
                else:
                    return False
        return True
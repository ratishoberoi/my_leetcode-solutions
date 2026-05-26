class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for char in s:
            stack.append(char) 
        for i in range(len(s)):
            s[i] = stack.pop()                            
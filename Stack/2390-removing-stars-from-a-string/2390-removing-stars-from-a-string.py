class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack+=i
        return "".join(stack)
        
            
            
        
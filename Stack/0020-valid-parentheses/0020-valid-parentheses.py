class Solution:
    def isValid(self, s: str) -> bool:

        parenthese = {
            '(':')',
            '{':'}',
            '[':']'
        }

        stack = []      # ( [ {
        
        for c in s:
            if c in parenthese:     # opening
                stack.append(c)
            else:                   # closing
                if not stack or c != parenthese[stack.pop()]:
                    return False
        return not stack 


    # Oct 5 2024 solution:
    
class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for c in s:
            if c in parentheses.keys():
                stack.append(c)
            else:
                if not stack or c != parentheses[stack[-1]]:
                    return False
                stack.pop()

        return not stack
        


        
   


        

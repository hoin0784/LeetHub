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
        


        
   


        
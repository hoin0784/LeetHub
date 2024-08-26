class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        stack = []

        def generate(openParen,closeParen):
            if openParen == closeParen == n :
                ans.append("".join(stack))
                return

            if openParen < n:
                stack.append("(")
                generate(openParen + 1 , closeParen)
                stack.pop()

            if closeParen < openParen:
                stack.append(")")
                generate(openParen, closeParen + 1)
                stack.pop()

        generate(0,0)
            
        return ans
        



    
            



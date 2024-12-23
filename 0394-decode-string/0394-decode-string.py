class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        cur_String = ""
        cur_Num = 0

        for c in s:
            if c.isdigit():
                cur_Num = 10 * cur_Num + int(c)
            elif c == "[":
                stack.append(cur_String)
                stack.append(cur_Num)
                cur_String = ""
                cur_Num = 0

            elif c == "]":
                num = stack.pop()
                prev_string = stack.pop()
                cur_String = prev_string + num * cur_String

            else:
                cur_String += c
        
        return cur_String
            

        
                
        


        
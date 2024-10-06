class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split by '/'.
        # Use a stack and ignore empty spaces and '.'; pop on double dot '..'

        stack = []
        path = path.split("/")

        for elem in path:      
            if stack and elem == "..":
                stack.pop()
            elif elem not in [".","",".."]:     # Append the file into stack
                stack.append(elem)
        
        print(stack)
        return '/' + '/'.join(stack)

        

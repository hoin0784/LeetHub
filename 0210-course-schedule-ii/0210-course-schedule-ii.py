class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # ex 2)
        # 0 : []
        # 1 : [0]
        # 2 : [0]
        # 3 : [1,2]

        preMap = {c : [] for c in range(numCourses)}
        
        for course, pre in prerequisites:                       
            preMap[course].append(pre)
        
        output = []

        finished, traversing = set(), set()

        def dfs(course):
            
            if course in traversing:        # The case that course is cycling
                return False
            if course in finished:          # help not to be repeated
                return True

            traversing.add(course)       # add the course in traversing..

            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
                
            traversing.remove(course)   # remove the list of course (prerequisite is empty case)
            finished.add(course)
            output.append(course)
            
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

        

            
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        
        def dfs(i):
            if i == len(nums):
                answer.append(path.copy())
                return
            
            path.append(nums[i])

            dfs(i+1)
            path.pop()
            dfs(i+1)

        path = []
        answer = []
        dfs(0)

        return answer


        


   
        
      
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        numCheck = set()
        ans = []
        
        def dfs(path):
            if len(nums) == len(path):
                ans.append(path.copy())
                return

            for num in nums:
                if num in numCheck:
                    continue
                numCheck.add(num)
                path.append(num)
                dfs(path)
                path.pop()
                numCheck.remove(num)

        dfs([])

        return ans
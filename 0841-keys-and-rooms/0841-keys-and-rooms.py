class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()

        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for key in rooms[i]:
                dfs(key)
        dfs(0)
        
        return len(visit) == len(rooms)

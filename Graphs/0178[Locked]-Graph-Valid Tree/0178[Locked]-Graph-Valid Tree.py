from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(n)}

        for n1,n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        
        visit = set()

        def dfs(i,prev):
            if i in visit:                  # if "i" happends one more time, it has loop
                return False                # return False
            
            visit.add(i)

            for edge in preMap[i]:
                if edge == prev:            # For preventing not going back to original node
                    continue
                if not dfs(edge,i):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visit)
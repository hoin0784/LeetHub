class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        path = []

        def dfs(node):
            path.append(node)  # 현재 노드를 경로에 추가
            if node == len(graph) - 1:  # 마지막 노드에 도달하면 경로를 결과에 추가
                output.append(path[:])  # 현재 경로를 복사해서 추가
            else:
                for neighbor in graph[node]:  # 현재 노드에서 가능한 모든 다음 노드로 이동
                    dfs(neighbor)
            path.pop()  # 현재 노드를 경로에서 제거 (백트래킹)

        dfs(0)  # 시작 노드는 0
        return output
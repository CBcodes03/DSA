class Solution:
    '''
      problem:- https://leetcode.com/problems/all-paths-from-source-to-target/
    '''
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1
        def dfs(node, path):
            if node == target:
                res.append(path[:])
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        dfs(0, [0])
        return res

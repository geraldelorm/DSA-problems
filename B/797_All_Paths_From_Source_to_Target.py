class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list = {}

        for i in range(len(graph)):
           adj_list[i] = set(graph[i]) 


        paths = []
        def traverse(source, target, path):
            if source == target:
                paths.append(list(path))
                return

            for nei in adj_list[source]:
                path.append(nei)
                traverse(nei, target, path)
                path.pop()

        traverse(0, len(graph) - 1, [0])
        return paths

    # TC: O(2^N.N) #number of paths = 2^n-1 - 1
    # SC: O(N)
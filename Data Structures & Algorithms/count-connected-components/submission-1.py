class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        n_components = 0

        visited = [False] * n

        def bfs(i):    
            
            queue = deque([i])

            while queue:

                curr_node = queue.popleft()

                for adj_node in adj_list[curr_node]:
                    if not visited[adj_node]:
                        visited[adj_node] = True
                        queue.append(adj_node)

        for i in range(n):
            if not visited[i]:
                bfs(i)
                n_components+=1

        return n_components
        

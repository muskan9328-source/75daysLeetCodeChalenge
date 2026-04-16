from collections import deque

class Solution:
    def specialNodes(self, n, edges, x, y, z):   # 👈 yaha change kiya
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            dist = [-1] * n
            queue = deque([start])
            dist[start] = 0

            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        queue.append(nei)
            return dist

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        count = 0
        for i in range(n):
            a, b, c = sorted([dx[i], dy[i], dz[i]])
            if a*a + b*b == c*c:
                count += 1

        return count
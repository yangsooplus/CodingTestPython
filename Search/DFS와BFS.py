from collections import deque

def dfs(graph, start, visited):
  print(start+1, end=' ')
  visited[start] = True
  for v in graph[start]:
    if not visited[v]:
      dfs(graph, v, visited)


def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    pop = queue.popleft()
    print(pop+1, end=' ')
    for v in graph[pop]:
      if not visited[v]:
        queue.append(v)
        visited[v] = True

  


n, m, v = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(m):
  s, d = map(int, input().split())
  graph[s-1].append(d-1)
  graph[d-1].append(s-1)

for i in range(n):
  graph[i].sort()

visited = [False]*n

dfs(graph, v-1, visited)

print()

visited = [False]*n

bfs(graph, v-1, visited)

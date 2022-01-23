def DFS(graph, root, cnt):
  visited[root] = True
  for v in graph[root]:
    if not visited[v]:
      cnt = DFS(graph, v, cnt+1)
      
  return cnt

n = int(input())
e = int(input())

graph = [[] for i in range(n)]
visited = [False]*n

for i in range(e):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

print(DFS(graph, 0, 0))

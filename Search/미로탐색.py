from collections import deque

def BFS(graph, n, m):
  cnt = 1
  queue = deque([[0, 0]])
  graph[0][0] = -1
  while queue:
    #PrintGraph(graph, n, m)

    pop = queue.popleft()
    cnt = graph[pop[0]][pop[1]]
    if cnt == -1: cnt = 1

    if pop[0] == n-1 and pop[1] == m-1:
      return graph[n-1][m-1]

    if pop[0] < n-1 and graph[pop[0]+1][pop[1]] == 1:
      queue.append([pop[0]+1, pop[1]])
      graph[pop[0]+1][pop[1]] = cnt+1
    if pop[1] < m-1 and graph[pop[0]][pop[1]+1] == 1:
      queue.append([pop[0], pop[1]+1])
      graph[pop[0]][pop[1]+1] = cnt+1
    if pop[0] > 0 and graph[pop[0]-1][pop[1]] == 1:
      queue.append([pop[0]-1, pop[1]])
      graph[pop[0]-1][pop[1]] = cnt+1
    if pop[1] > 0 and graph[pop[0]][pop[1]-1] == 1:
      queue.append([pop[0], pop[1]-1])
      graph[pop[0]][pop[1]-1] = cnt+1

def PrintGraph(graph, n, m):
  for i in range(n):
    for j in range(m):
      print( graph[i][j], end=' ')
    print()
  print()
  return    

n, m = map(int, input().split())
graph = []


for i in range(n):
  graph.append(list(map(int, input())))

print(BFS(graph, n, m))


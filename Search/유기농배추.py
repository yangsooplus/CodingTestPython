def dfs(garden, x, y, m, n):
  garden[x][y] = 2
  
  if x > 0 and garden[x-1][y] == 1:
    dfs(garden, x-1, y, m, n)
  
  if x < n-1 and garden[x+1][y] == 1:
    dfs(garden, x+1, y, m, n)

  if y > 0 and garden[x][y-1] == 1:
    dfs(garden, x, y-1, m, n)
  
  if y < m-1 and garden[x][y+1] == 1:
    dfs(garden, x, y+1, m, n)


def PrintGarden(gar, m, n):
  print("-----------------")
  for i in range(n):
    for j in range(m):
      print(gar[i][j], end=' ')
    print()
  print("-----------------")



t = int(input())

for tests in range(t):
  m, n, k = map(int, input().split())
  garden = [[0 for j in range(m)] for i in range(n)]
  for i in range(k):
    y, x = map(int, input().split())
    garden[x][y] = 1

  #PrintGarden(garden, m, n)

  cnt = 0
  for i in range(n):
    for j in range(m):
      if garden[i][j] == 1:
        dfs(garden, i, j, m, n)
        cnt += 1
        #PrintGarden(garden, m, n)
  print(cnt)


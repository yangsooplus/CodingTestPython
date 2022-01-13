from collections import deque


def bfs(garden, x, y, m, n):
  queue = deque([[x, y]])
  garden[x][y] = 2
  while queue:
    pop = queue.popleft()
    ix, iy = pop[0], pop[1]

    if ix > 0 and garden[ix-1][iy] == 1:
      queue.append([ix-1, iy])
      garden[ix-1][iy] = 2

    if ix < n-1 and garden[ix+1][iy] == 1:
      queue.append([ix+1, iy])
      garden[ix+1][iy] = 2

    if iy > 0 and garden[ix][iy-1] == 1:
      queue.append([ix, iy-1])
      garden[ix][iy-1] = 2

    if iy < m-1 and garden[ix][iy+1] == 1:
      queue.append([ix, iy+1])
      garden[ix][iy+1] = 2

  


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
        bfs(garden, i, j, m, n)
        cnt += 1
        #PrintGarden(garden, m, n)
  print(cnt)


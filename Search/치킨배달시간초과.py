from collections import deque
import copy
import itertools

def printArr(arr):
  for ar in arr:
    print(ar)
  print()

def ChickFS(a, i, j, n):
  arr = copy.deepcopy(a)
  queue = deque([(i, j)])
  arr[i][j] = -1

  while queue:
    pop = queue.popleft()
    i, j = pop[0], pop[1]
      
    #printArr(arr)
    
    if i > 0 and arr[i-1][j] >= 0:
      if arr[i-1][j] == 2:
        return -(arr[i][j])
      queue.append((i-1, j))
      arr[i-1][j] = arr[i][j]-1
      
    if i < n-1 and arr[i+1][j] >= 0:
      if arr[i+1][j] == 2:
        return -(arr[i][j])
      queue.append((i+1, j))
      arr[i+1][j] = arr[i][j]-1
      
    if j > 0 and arr[i][j-1] >= 0:
      if arr[i][j-1] == 2:
        return -(arr[i][j])
      queue.append((i, j-1))
      arr[i][j-1] = arr[i][j]-1
      
    if j < n-1 and arr[i][j+1] >= 0:
      if arr[i][j+1] == 2:
        return -(arr[i][j])
      queue.append((i, j+1))
      arr[i][j+1] = arr[i][j]-1


n, m = map(int, input().split(' '))

arr = []
for i in range(n):
  arr.append(list(map(int, input().split(' '))))

chickcnt = 0
for ar in arr:
  chickcnt += ar.count(2)

if chickcnt > m:
  # 치킨집 위치 추출하고 0으로 바꿔두기
  chicken = []
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 2:
        chicken.append((i, j))
        arr[i][j] = 0

  nCr = itertools.combinations(chicken, m)
  minchickDist = 99999
  
  for iter in nCr:
    arrr = copy.deepcopy(arr)
    for iterele in iter:
      arrr[iterele[0]][iterele[1]] = 2

    
    chickDist = 0
    for i in range(n):
      for j in range(n):
        if arr[i][j] == 1:
          chickDist += ChickFS(arrr, i, j, n)

    
    minchickDist = min(minchickDist, chickDist)
  print(minchickDist)

else:
  chickDist = 0
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 1:
        chickDist += ChickFS(arr, i, j, n)
        print(chickDist)

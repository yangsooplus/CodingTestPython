import itertools


def calChickDist(h, chicks): # 집 1개, chicks 선택 치킨집들
  minDist = 99999
  for c in chicks: # 모든 치킨 집과 치킨거리 계산
    dist = abs(c[0]-h[0]) + abs(c[1]-h[1]) 
    minDist = min(minDist, dist) #가장 작은 거리가 이 집 h의 최소 치킨 거리 
  return minDist


n, m = map(int, input().split(' '))
arr = [] #지도
chicken = [] #모든 치킨집 좌표
house = [] #모든 집 좌표

# 입력
for i in range(n):
  arr.append(list(map(int, input().split(' '))))

#치킨집, 집 추출
for i in range(n):
  for j in range(n):
    if arr[i][j] == 2:
      chicken.append((i, j))
    elif arr[i][j] == 1:
      house.append((i, j))

# 최대 개수보다 많다면? m개만 뽑는다
if len(chicken) > m:
  nCr = itertools.combinations(chicken, m)
  minchickDist = 99999
  
  for iter in nCr: #치킨집 m개의 쌍 추출
    chickDist = 0
    for h in house: #모든 집으로부터의 치킨거리 계산
      chickDist += calChickDist(h, iter)
    minchickDist = min(minchickDist, chickDist)
  print(minchickDist) #최소 치킨거리 

else:
  chickDist = 0
  for h in house:
    chickDist += calChickDist(h, chicken)
  print(chickDist) #치킨 거리

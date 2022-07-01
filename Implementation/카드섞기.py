def isVaild(arr):
  for i in range(len(arr)):
    if arr[i] != i%3:
      return False
  return True

def shuffle(P, S, n):
  sP = [-1 for i in range(n)]

  for i in range(n):
    sP[S[i]] = P[i]

  return sP
  
def possible(P, S, n):
  for i in range(n):
    if i == S[i]:
      if i%3 != P[i]%3:
        return False
  return True
  
n = int(input())
P = list(map(int, input().split(' ')))
S = list(map(int, input().split(' ')))
cnt = 0

if possible(P, S, n):
  while not isVaild(P):
    P = shuffle(P, S, n)
    cnt += 1  
  
  print(cnt)
else:
  print(-1)

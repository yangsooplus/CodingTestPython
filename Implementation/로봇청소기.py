n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))

arr = []
for i in range(n):
  arr.append(list(map(int, input().split(' '))))

a2 = 0
cleanCnt = 0
while True:
  #1. 현재 위치를 청소
  if arr[r][c] == 0:
    arr[r][c] = 2
    cleanCnt += 1
    a2 = 0
  elif a2 > 3:
    a2 = 0
    if d == 0:
      r = r+1
    elif d == 1:
      c = c-1
    elif d == 2:
      r = r-1
    elif d == 3:
      c = c+1
    
    if arr[r][c] == 1:
      break
      

  if d == 0:
    d = 3
    if arr[r][c-1] == 0:
      c = c-1
    else:
      a2 += 1
  elif d == 1:
    d = 0
    if arr[r-1][c] == 0:
      r = r-1
    else:
      a2 += 1
  elif d == 2:
    d = 1
    if arr[r][c+1] == 0:
      c = c+1
    else:
      a2 += 1
  elif d == 3:
    d = 2
    if arr[r+1][c] == 0:
      r = r+1
    else:
      a2 += 1

print(cleanCnt)
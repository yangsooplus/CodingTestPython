n = int(input())
bigger = list(map(int, input().split(' ')))
row = [0 for i in range(n)]

for i in range(n):
  bigCnt = 0 # 0이거나 나보다 크면 +1

  for j in range(n):
    if row[j] == 0 and bigCnt == bigger[i]:
      row[j] = i+1
      break
    
    if row[j] == 0 or row[j] > i+1:
      bigCnt += 1

  
for i in range(n):
  print(row[i], end=" ")
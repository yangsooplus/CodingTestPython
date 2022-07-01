A, B = input().split(' ')
lenA = len(A)
n = len(B) - lenA + 1

match = 0
for i in range(n):
  subB = B[i:i+lenA]
  cnt = 0
  for j in range(lenA):
    if A[j] == subB[j]:
      cnt += 1

  match = max(match, cnt)
  
print(lenA - match)
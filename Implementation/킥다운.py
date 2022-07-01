# P 와 C가 맞물리는지 
def kickDown(P, C):
  for i in range(len(P)):
    if P[i] == '2' and C[i] == '2':
      return False
  return True
  
A = input()
B = input()

# A 안에서 비교할 횟수
n = len(A) - len(B) +1

# A > B 상태 유지
if n < 0:
  n *= -1
  A, B = B, A

result = -1

for i in range(n):
  subA = A[i:i+len(B)]
  if kickDown(subA, B):
    result = len(A)
    break

if result > 0:
  print(result)
else:
  for i in range(1, len(B)):
    frontB = B[i:]
    if kickDown(A[:len(frontB)], frontB):
      result = len(A) + i
      break
    
    rearB = B[:-i]
    if kickDown(A[-len(rearB):], rearB):
      result = len(A) + i
      break

  if result > 0:
    print(result)
  else:
    print(len(A)+len(B))
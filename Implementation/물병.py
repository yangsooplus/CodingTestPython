n, k = map(int, input().split(' '))
buy = 0
value = 1


while True:
  if n//2 == k and n%2 == 0:
    break

  mox = n//2
  na = n%2

  if na == 1:
    na = 0
    mox += 1
    buy += value

  value *= 2
  n = mox

  

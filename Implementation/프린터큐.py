from collections import deque
cases = int(input())

for k in range(cases):
  n, target = map(int, input().split(' '))
  arr = deque(list(map(int, input().split(' '))))

  cnt = 0
  max_n = max(arr)
  while target != -1:

    pop = arr.popleft()
    target -= 1

    if pop == max_n:
      cnt += 1
      if len(arr) == 0: 
        break
      max_n = max(arr)
    else:
      arr.append(pop)
      if target == -1:
        target = len(arr)-1

  print(cnt)
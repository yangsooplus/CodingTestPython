from collections import deque

def joinStr(arr):
  new_str = ','.join(arr)
  new_str = '[' + new_str + ']'
  print(new_str, end = '\n')


def funcAC(arr, st, length):
  R = 0
  
  for s in st:
    if s == 'R':
      R += 1
    elif s == 'D':
      if length > 0:
        if R%2 == 0:
          arr.popleft()
        else:
          arr.pop()
        length -= 1
        
      else:
        print('error', end="\n")
        return

  if R%2==1:
    arr.reverse()
  joinStr(arr)
        
t = int(input())

for i in range(t):
  do = input()
  length = int(input())
  iarr = input()
  iarr = iarr[1:-1]
  iarr = iarr.replace(' ', '')
  arr = deque(list(iarr.split(',')))
  funcAC(arr, do, length)
  
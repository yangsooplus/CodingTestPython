n = int(input())
groupNum = n
for i in range(n):
  nope = []
  st = input()

  last = ''
  if len(st) == 1:
    continue
    
  for s in st:
    if last == '':
      last = s
    elif s in nope:
      groupNum -= 1
      break
    elif s != last:
      nope.append(last)
      last = s

print(groupNum)
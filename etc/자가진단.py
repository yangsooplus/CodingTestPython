arr = list(map(int, input().split(' ')))

arrDict = {}
order = []


for num in arr:
  if not num in arrDict:
    arrDict[num] = 1
    order.append(num)
  else:
    arrDict[num] += 1

result = []

result = list(filter(lambda x:x > 1, arrDict.values()))

if result:
  print(result)  
else:
  print([-1])
import sys
put = sys.stdin.readline

n = int(put())
num = []
for i in range(n):
  num.append(int(put()))

sansul = round(sum(num)/n)
num.sort()
center = num[n//2]

cntDict = {}
for s in num:
  if not s in cntDict:
    cntDict[s] = 0
  else:
    cntDict[s] += 1

modeList = [k for k, v in cntDict.items() if max(cntDict.values()) == v]

if len(modeList) == 1:
  mode = modeList[0]
else:
  mode = modeList[1]

range = max(num) - min(num)
print(sansul)
print(center)
print(mode)
print(range)
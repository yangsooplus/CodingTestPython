def isNum(ch):
  return ord('0') <= ord(ch) and ord('9') >= ord(ch)

def isABC(ch):
  return ord('A') <= ord(ch) and ord('Z') >= ord(ch)

def Dto36(num):
  result = ''
  while num > 0:
    modulo = num%36
    if modulo < 10:
      result = str(modulo) + result
    else:
      result = chr(modulo - 10 + ord('A')) + result
    num //= 36
  return result

def split36toD(num36):
  result = []
  # A = 10
  # alpha - ord('A') + 10 

  for ch in num36:                     
    if isNum(ch):
      result.append(int(ch))
    elif isABC(ch):
      result.append(ord(ch)-ord('A')+10)
  
  return result

def cal36toD(dlist):
  result = 0
  ten = 0
  
  while dlist:
    result += dlist.pop()*(36**ten)
    ten += 1
  
  return result

n = int(input())
wordList = []
for i in range(n):
  num36 = input()
  wordList.append(split36toD(num36))
k = int(input())

print(wordList)

# 큰 수를 만드는 방법 (우선순위)
# 1. 자리수가 큰 녀석을 Z으로 바꾼다
# 2. 그 안에서도 작은 수를 바꾼다. 
# 3. 그 안에서도 많이 나오는 녀석을 바꾼다.

# 아이디어: 우선순위대로 큐에 넣어서 k개만큼 뽑아쓰면 어떨까
# 중복은 무시하고 뽑고 한번에 바꾸기


max_len = len(wordList[0])
max_idx = []
for i in range(n):
  if len(wordList[i]) > max_len:
    max_len = len(wordList[i])
    max_idx = [i]
  elif len(wordList[i]) == max_len:
    max_idx.append(i)

print(max_idx)
prior = []


for w in wordList:
  target = []
  if len(w) == max_len:
    target.append(w.pop(0))

  target.sort()
  prior += target
  max_len -= 1


'''
sumD = 0
for i in range(n):
  sumD += cal36toD(wordList[i])

print(Dto36(sumD))
'''
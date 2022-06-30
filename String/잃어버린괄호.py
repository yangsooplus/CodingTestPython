def isNum(ch):
  return ord('0') <= ord(ch) and ord('9') >= ord(ch)

st = input()
stList = []
# - 뒤에 나오는 총합이 가장 크게
# - 뒤에 나오는 + 들은 모두 괄호로 묶는다

cutst = ''
for i in range(len(st)):
  if st[i] != '+' and st[i] != '-':
    cutst += st[i]
  else:
    stList.append(cutst)
    stList.append(st[i])
    cutst = ''
stList.append(cutst)
      
Minus = False
total = 0
for ele in stList:
  if ele == '-':
    Minus = True
    continue
  elif ele != '+':
    if Minus:
      total -= int(ele)
    else:
      total += int(ele)

  
print(total)
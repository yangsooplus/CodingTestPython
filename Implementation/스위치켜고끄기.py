def onoff(light, i):
  if light[i] == '0':
      light[i] = '1'
  else:
      light[i] = '0'

def boy(light, num):
  for i in range(num, len(light)+1, num):
    onoff(light, i-1)
  return light

def girl(light, num):
  onoff(light, num)
  l = num-1
  r = num+1
  while l > -1 and r < len(light):
    if light[l] == light[r]:
      onoff(light, l)
      onoff(light, r)
      l -= 1
      r += 1
    else:
      break
  return light

n = int(input())
light = list(input().split(' '))
stuNum = int(input())

for i in range(stuNum):
  sex, num = map(int, input().split(' '))

  if sex == 1:
    light = boy(light, num)
  else:
    light = girl(light, num-1)

# 전구는 20개 단위로 출력한다!!!
# 문제를 잘 읽자!!!!!
for i in range(len(light)):
  print(light[i], end=" ")
  if i%20 == 19:
    print()

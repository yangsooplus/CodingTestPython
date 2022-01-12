def Rotate(gear, direc):
  if direc == 1:
    tmp = gear[0]
    gear[0] = gear[7]
    for i in range(7, 0, -1):
      gear[i] = gear[i-1]
    gear[1] = tmp
  elif direc == -1:
      tmp = gear[0]
      for i in range(7):
        gear[i] = gear[i+1]
      gear[7] = tmp


def printGear(gear):
  print("-------------------")
  for i in range(4):
    print(gear[i]);
  print("-------------------")

def UpdateGear(gear, gidx, direc, chain):  
  if gidx > 0 and chain != 2:
    if gear[gidx-1][2] != gear[gidx][6]:
      if gidx > 0:          
        UpdateGear(gear, gidx-1, -1*direc, 1)

  
  if gidx < 3 and chain != 1:
    if gear[gidx+1][6] != gear[gidx][2]:
      if gidx < 3:
        UpdateGear(gear, gidx+1, -1*direc, 2)
  
  
  Rotate(gear[gidx], direc)
  #print(gidx,"번 톱니가", direc, "방향으로 회전")


gear = []

for i in range(4):
  str = input()
  tmp_list = []
  for j in range(8):
    tmp_list.append(str[j])
  gear.append(tmp_list)

n = int(input())
for i in range(n):
  idx, d = map(int, input().split())
  UpdateGear(gear, idx-1, d, 0)
  #printGear(gear)

score = 0
if gear[0][0] == '1':
  score += 1

if gear[1][0] == '1':
  score += 2

if gear[2][0] == '1':
  score += 4
  
if gear[3][0] == '1':
  score += 8

print(score)
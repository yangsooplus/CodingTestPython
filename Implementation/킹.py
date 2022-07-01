def cvtPosN(pos):
  C = ord(pos[0]) - ord('A')

  rD = {"8":0, "7":1, "6":2, "5":3, "4":4, "3":5, "2":6, "1":7}
  R = rD[pos[1]]

  return (R, C)

def cvtPosA(pos):
  cvtPos = ""

  cvtPos += chr(pos[1] + ord('A')) 
  rD = {"8":0, "7":1, "6":2, "5":3, "4":4, "3":5, "2":6, "1":7}

  for k, v in rD.items():
    if v == pos[0]:
      cvtPos += k
      return cvtPos


def rangeCheck(tup):
  return tup[0] > -1 and tup[0] < 8 and tup[1] > -1 and tup[1] < 8

M = {'R': (0, 1), 'L':(0, -1), 'B':(1, 0), 'T':(-1, 0), 'RT':(-1, 1), 'LT':(-1, -1), 'RB':(1, 1), 'LB':(1, -1)}

king, stone, n = input().split(' ')
n = int(n)

king = cvtPosN(king)
stone = cvtPosN(stone)

for i in range(n):
  cmd = input()
  kpos = (king[0] + M[cmd][0], king[1] + M[cmd][1])
  spos = stone
  if kpos == stone:
    spos = (stone[0] + M[cmd][0], stone[1] + M[cmd][1])

  if rangeCheck(kpos) and rangeCheck(spos):
    king = kpos
    stone = spos

print(cvtPosA(king))
print(cvtPosA(stone))
  
import sys
m = int(sys.stdin.readline())
bit = 0b0

for i in range(m):
  line = sys.stdin.readline()
  if ' ' in line:
    do, num = line.strip().split(' ')
    num = int(num)
  else:
    do = line.strip()


  if do == "add":
    bit |= (1 << num) # num번째 비트를 1로 (1과 or연산)
  elif do == "check":
    if bit & (1 << num):
      print("1")
    else:
      print("0")
  elif do == "remove":
    bit &= ~(1 << num) # num번째 비트를 0으로 (0과 and 연산)
  elif do == "toggle":
    bit ^= (1 << num) # num번째 비트와 xor 연산
  elif do == "all":
    bit = 0b111111111111111111111
    # 1 << 21: 100000000000000000000
    # (1 << 21) - 1: 11111111111111111111
  elif do == "empty":
    bit = 0b0
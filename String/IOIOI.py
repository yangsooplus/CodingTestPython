n = int(input())
m = int(input())
st = input()

cnt = 0
ioicnt = 0
ilen = 2*n + 1
for i in range(0, len(st)-2, 1):
  if st[i] == 'I':
    if st[i+1] == 'O' and st[i+2] == 'I':
      ioicnt += 1
    else:
      ioicnt = 0

    if ioicnt*2+1 >= ilen:
      cnt += 1
  else:
    if st[i+1] != 'I':
      ioicnt = 0
  
print(cnt)
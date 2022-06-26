n, m = map(int, input().split(' '))
do = []
su = []

for i in range(n):
  a, b = map(int, input().split(' '))
  do.append(a)
  su.append(b)

do_grave = []
su_grave = []

gameCnt = 0

do_ground = do.pop()
do_grave.append(do_ground)
gameCnt += 1
su_ground = su.pop()
su_grave.append(su_ground)
gameCnt += 1

while True:
  
  if do_ground == 5 or su_ground == 5:
    do = do_grave[:] + su_grave[:] + do[:]
    do_grave = []
    su_grave = []
  elif do_ground + su_ground == 5:
    su = su_grave[:] + do_grave[:] + su[:]
    do_grave = []
    su_grave = []
    
  if gameCnt == m:
    break

  if not do: break
  do_ground = do.pop()
  do_grave.append(do_ground)
  gameCnt += 1
  
  if do_ground == 5 or su_ground == 5:
    
    do = do_grave[:] + su_grave[:] + do[:]
    do_grave = []
    su_grave = []
    if gameCnt == m:
      break
  elif do_ground + su_ground == 5:
    
    su = su_grave[:] + do_grave[:] + su[:]
    do_grave = []
    su_grave = []
    if gameCnt == m:
      break

  if gameCnt == m:
    break
  
  if not su: break
  su_ground = su.pop()
  su_grave.append(su_ground)
  gameCnt += 1

if len(do) > len(su):
  print('do')
elif len(do) < len(su):
  print('su')
else:
  print('dosu')

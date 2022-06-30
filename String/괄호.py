n = int(input())
for i in range(n):
  ps = input()
  stack = []
  for s in ps:
    if s == '(':
      stack.append(s)
    else:
      if len(stack) > 0 and stack[-1] == '(':
        stack.pop()
      else:
        print('NO')
        break
  else: 
    if stack:
      print('NO')
    else:
      print('YES')
st = input()
boom = input()
boomlen = len(boom)
stack = []

for s in st:
  stack.append(s)
  if len(stack) >= boomlen:
    if ''.join(stack[-boomlen:]) == boom:
        for i in range(boomlen):
          stack.pop()


if not stack:
  print('FRULA')
else:
  print(''.join(stack))
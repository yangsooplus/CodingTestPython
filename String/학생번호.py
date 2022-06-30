n = int(input())
stu = []
for i in range(n):
  stu.append(input())

for k in range(1, len(stu[0])+1):
  nums = []
  for i in range(n):
    num = stu[i][-k:]
    if num in nums:
      break
    else:
      nums.append(num)
  else: # 무사히 for문을 다 돌면
    break
print(k)
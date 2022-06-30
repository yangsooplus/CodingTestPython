P14 = [(0, 0), (0,1), (0,2), (0,3)]
P41 = [(0,0), (1,0), (2,0), (3,0)]
P22 = [(0,0), (1,0), (0,1), (1,1)]
P23 = [[(0,0), (0,1), (0,2), (1,0)], [(0,0), (0,1), (0,2), (1,2)], [(0,2), (1,0), (1,1), (1,2)], [(0,0), (1,0), (1,1), (1,2)], [(0,1), (0,2), (1,0), (1,1)], [(0,0), (0,1), (1,1), (1,2)], [(0,0), (0,1), (0,2), (1,1)], [(0,1), (1,0), (1,1), (1,2)]]
P32 = [[(0,0), (1,0), (2,0), (2,1)], [(0,1), (1,1), (2,1), (2,0)], [(0,0), (0,1), (1,1), (2,1)], [(0,0), (0,1), (1,0), (2,0)], [(0,0), (1,0), (1,1), (2,1)], [(0,1), (1,0), (1,1), (2,0)], [(0,0), (1,0), (1,1), (2,0)], [(0,1), (1,0), (1,1), (2,1)]]

max_sum = 0

n, m = map(int, input().split(' '))
arr = []
for i in range(n):
  arr.append(list(map(int, input().split(' '))))

# 1 by 4
for i in range(n):
  for j in range(m - 3):
    sum_ = arr[i+P14[0][0]][j+P14[0][1]] + arr[i+P14[1][0]][j+P14[1][1]] + arr[i+P14[2][0]][j+P14[2][1]] + arr[i+P14[3][0]][j+P14[3][1]]

    max_sum = max(max_sum, sum_)

# 4 by 1
for i in range(n - 3):
  for j in range(m):
    sum_ = arr[i+P41[0][0]][j+P41[0][1]] + arr[i+P41[1][0]][j+P41[1][1]] + arr[i+P41[2][0]][j+P41[2][1]] + arr[i+P41[3][0]][j+P41[3][1]]

    max_sum = max(max_sum, sum_)

# 2 by 2
for i in range(n - 1):
  for j in range(m - 1):
    sum_ = arr[i+P22[0][0]][j+P22[0][1]] + arr[i+P22[1][0]][j+P22[1][1]] + arr[i+P22[2][0]][j+P22[2][1]] + arr[i+P22[3][0]][j+P22[3][1]]

    max_sum = max(max_sum, sum_)

# 2 by 3
for i in range(n - 1):
  for j in range(m - 2):
    for P in P23:
      sum_ = arr[i+P[0][0]][j+P[0][1]] + arr[i+P[1][0]][j+P[1][1]] + arr[i+P[2][0]][j+P[2][1]] + arr[i+P[3][0]][j+P[3][1]]  

      max_sum = max(max_sum, sum_)

# 3 by 2
for i in range(n - 2):
  for j in range(m - 1):
    for P in P32:
      sum_ = arr[i+P[0][0]][j+P[0][1]] + arr[i+P[1][0]][j+P[1][1]] + arr[i+P[2][0]][j+P[2][1]] + arr[i+P[3][0]][j+P[3][1]]  

      max_sum = max(max_sum, sum_)

print(max_sum)
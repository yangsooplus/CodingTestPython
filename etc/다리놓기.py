t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  mul_m = 1
  for j in range(n):
    mul_m *= m - j

  mul_n = 1
  for j in range(n):
    mul_n *= n - j
  print(mul_m//mul_n)
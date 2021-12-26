n = int(input())
call = list(map(int, input().split()))
min = call[0]

for i in range(n):
    if min > call[i]:
        min = call[i]
print(min)

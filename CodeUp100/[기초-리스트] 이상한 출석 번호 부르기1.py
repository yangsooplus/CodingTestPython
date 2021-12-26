n = int(input())
stu = [0 for i in range(23)]

call = list(map(int, input().split()))

for i in range(n):
    stu[call[i]-1] += 1

for i in range(23):
    print(stu[i], end=" ")
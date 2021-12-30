n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split())) #b는 재배열 금지

a.sort(reverse=True)

result = [0 for i in range(n)]
flag = [0 for i in range(n)]

for i in range(n):
    min_mul = -1

    for j in range(n):
        if flag[j] == 1:
            continue

        if min_mul < 0:
            min_mul = a[i]*b[j]
            mindex = j

        if a[i]*b[j] < min_mul:
            min_mul = a[i]*b[j]
            mindex = j

    result[mindex] = a[i]
    flag[mindex] = 1

total = 0
for i in range(n):
    total += result[i]*b[i]
print(total)

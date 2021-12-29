n = int(input())
hlist = []
times = []
cnt = 0

for i in range(n):
    s, e = map(int, input().split())
    hlist.append([s, e])

hlist.sort(key=lambda x: (x[1], x[0]))

prev_end = hlist[0][1]
for i in range(1, n):
    curr_start = hlist[i][0]
    if curr_start >= prev_end:
        cnt += 1
        prev_end = hlist[i][1]

print(cnt+1)

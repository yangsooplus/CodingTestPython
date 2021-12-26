n = int(input())

call = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(call[i], end=" ")

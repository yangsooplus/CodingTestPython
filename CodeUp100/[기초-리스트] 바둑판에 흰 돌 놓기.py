badoc = [[0 for j in range(19)] for i in range(19)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    badoc[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(badoc[i][j], end=" ")
    print()

badoc = []

for i in range(19):
    row = list(map(int, input().split()))
    badoc.append(row)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if badoc[x-1][j] == 0:
            badoc[x - 1][j] = 1
        else:
            badoc[x - 1][j] = 0

    for j in range(19):
        if badoc[j][y-1] == 0:
            badoc[j][y-1] = 1
        else:
            badoc[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(badoc[i][j], end=" ")
    print()
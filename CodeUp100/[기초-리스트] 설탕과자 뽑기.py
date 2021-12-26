a, b = map(int, input().split())
sugar = [[0 for i in range(b)] for j in range(a)]
n = int(input())

for i in range(n):
    len, dir, x, y = map(int, input().split())
    for j in range(len):
        sugar[x - 1][y - 1] = 1
        if dir == 0: y+=1
        else: x+=1

for i in range(a):
    for j in range(b):
        print(sugar[i][j], end=" ")
    print()

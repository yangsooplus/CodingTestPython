n = int(input())
pouch = 0

for i in range(n//5, -1, -1):
    if (n - 5*i) % 3 == 0:
        pouch = (n - 5*i)//3 + i
        break

if pouch == 0:
    print(-1)
else:
    print(pouch)

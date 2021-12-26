route = []
for i in range(10):
    row = list(map(int, input().split()))
    route.append(row)

curr = route[1][1]
route[1][1] = 9
ant_x = 1
ant_y = 1

while curr != 2:
    if route[ant_y][ant_x+1] != 1:
        ant_x += 1
        curr = route[ant_y][ant_x]
        route[ant_y][ant_x] = 9
    elif route[ant_y+1][ant_x] != 1:
        ant_y += 1
        curr = route[ant_y][ant_x]
        route[ant_y][ant_x] = 9
    else:
        break

    if curr == 2: break

for i in range(10):
    for j in range(10):
        print(route[i][j], end =" ")
    print()

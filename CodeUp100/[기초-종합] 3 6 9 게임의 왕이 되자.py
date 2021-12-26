n = int(input())

for i in range(1, n+1):
    flag = 0 #박수 치면 1
    num = i
    while i > 0:
        if i%10 == 3 or i%10 == 6 or i%10 == 9:
            print('X', end='')
            flag = 1
        i //= 10

    if flag == 0:
        print(num, end='')

    print(end=' ')


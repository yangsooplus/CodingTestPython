n = int(input())

if n//3 == 1:
    season = "spring"
elif n//3 == 2:
    season = "summer"
elif n//3 == 3:
    season = "fall"
else:
    season = "winter"

print(season)
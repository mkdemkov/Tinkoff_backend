n, s = map(int, input().split())
best = 0
guns = [int(num) for num in input().split()]
for gun in guns:
    if gun <= s and gun > best:
        best = gun
print(best)
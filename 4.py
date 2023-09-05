m, n = map(int, input().split())
money = [int(num) for num in input().split()]
money.extend(money)
money.sort(reverse=True)
cur_sum = 0
res = []
flag = True
for num in money:
    cur_sum += num
    if cur_sum > m:
        flag = False
    elif cur_sum == m:
        res.append(num)
        break
    else:
        res.append(num)
if flag and cur_sum == m:
    print(len(res))
    print(" ".join(map(str, res)))
else:
    print(-1)
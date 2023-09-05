from collections import defaultdict
n = int(input())
a = [int(num) for num in input().split()]
b = [int(num) for num in input().split()]
l = 0
r = len(a) - 1
i = 0
while i < n:
    if a[i] != b[i]:
        l = i
        break
    i += 1
i = len(a) - 1
while i >= 0:
    if a[i] != b[i]:
        r = i
        break
    i -= 1
a_dict = defaultdict(int)
b_dict = defaultdict(int)
i = l
while i <= r:
    a_dict[int(a[i])] += 1
    b_dict[int(b[i])] += 1
    i += 1
if a_dict.keys() != b_dict.keys():
    print("NO")
else:
    flag = True
    for key, val in a_dict.items():
        if val != b_dict[key]:
            flag = False
    if not flag:
        print("NO")
    else:
        is_b_sorted = all(b[i] <= b[i + 1] for i in range(l, r))
        if is_b_sorted:
            print("YES")
        else:
            print("NO")
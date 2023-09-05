class Spirit:
    def __init__(self, ghost, count):
        self.ghost = ghost
        self.count = count

class Bands:
    def __init__(self, n):
        self.n = n
        self.gangs = [[] for _ in range(n)]
        for i in range(n):
            pair = Spirit(i + 1, 1)
            self.gangs[i].append(pair)

    def process(self, x, y):
        list_x = []
        list_y = []
        f = -1
        s = -1
        for i in range(len(self.gangs)):
            if list_x and list_y:
                break
            for j in range(len(self.gangs[i])):
                if not list_x and self.gangs[i][j].ghost == x:
                    list_x = self.gangs[i]
                    f = i
                if not list_y and self.gangs[i][j].ghost == y:
                    list_y = self.gangs[i]
                    s = i

        if s > f:
            del self.gangs[f]
            s -= 1
            del self.gangs[s]
        else:
            del self.gangs[s]
            f -= 1
            del self.gangs[f]

        for pair in list_x:
            pair.count += 1

        for pair in list_y:
            pair.count += 1

        self.gangs.append(list_x + list_y)

    def check(self, x, y):
        list_x = []
        for i in range(len(self.gangs)):
            for j in range(len(self.gangs[i])):
                if self.gangs[i][j].ghost == x:
                    list_x = self.gangs[i]
                    break

        if list_x:
            for pair in list_x:
                if pair.ghost == y:
                    return True

        return False

    def get_count(self, x):
        ret = -1
        for i in range(len(self.gangs)):
            for j in range(len(self.gangs[i])):
                if self.gangs[i][j].ghost == x:
                    ret = self.gangs[i][j].count

        return ret


n, m = map(int, input().split())
bands = Bands(n)
res = []
for _ in range(m):
    inp = [int(num) for num in input().split()]
    if inp[0] == 1:
        x1, y1 = inp[1], inp[2]
        bands.process(x1, y1)
    elif inp[0] == 2:
        x2, y2 = inp[1], inp[2]
        if bands.check(x2, y2):
            res.append("YES")
        else:
            res.append("NO")
    elif inp[0] == 3:
        x3 = inp[1]
        res.append(str(bands.get_count(x3)))
print("\n".join(res))
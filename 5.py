from collections import defaultdict

def dfs(graph: defaultdict, v: int, visited: [], x: int = -1):
    visited[v - 1] = True
    for neib in graph[v]:
        if neib[1] <= x:
            continue
        if not visited[neib[0] - 1]:
            dfs(graph, neib[0], visited, x)

def binSearch(l:int, r:int, graph: defaultdict, states: int, n: int) -> int:
    best = 0
    while l <= r:
        middle = (l + r) // 2 # текущий x
        new_states = 0
        visited = [False] * n
        for key, val in graph.items():
            if not visited[key - 1]:
                new_states += 1
                dfs(graph, key, visited, middle)

        if new_states == states:
            if middle > best:
                best = middle
            l = middle + 1
        else:
            r = middle - 1

    return best


n, m = map(int, input().split())
i = 0
graph = defaultdict(int)
for i in range(1, n+1):
    graph[i] = []

i = 0
max = -1
while i < m:
    v, u, w = map(int, input().split())
    if w > max:
        max = w
    graph[v].append((u, w))
    graph[u].append((v, w))
    i += 1

states = 0
visited = [False] * n
for key, val in graph.items():
    if not visited[key - 1]:
        states += 1
        dfs(graph, key, visited)


# теперь пройдемся по всем возможным значениям x в диапазоне [min_edge, max_edge]
print(binSearch(1, max, graph, states, n))
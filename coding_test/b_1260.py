from collections import deque

def dfs(V):
    visited1[V] = 1
    print(V, end=' ')
    
    for i in range(1, N+1):
        if visited1[i] == 0 and graph[V][i] == 1:
            dfs(i)

def bfs(V):
    qu = deque([V])
    visited2[V] = 1

    while qu:
        V = qu.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[V][i] == 1:
                qu.append(i)
                visited2[i] = 1


N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0]*(N+1)
visited2 = [0]*(N+1)

dfs(V)
print()
bfs(V)
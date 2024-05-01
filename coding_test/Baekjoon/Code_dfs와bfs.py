## Backjoon Solved.ac Q.1260

from collections import deque

n, m, v = map(int, input().split())
visited_dfs = [0]*(n+1)
visited_bfs = visited_dfs.copy()

# Graph 틀 생성
graph = [[0]*(n+1) for _ in range(n+1)]

# 간선 정보 받아오기
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def DFS(v):
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if visited_dfs[i]==0 and graph[v][i]==1:
            DFS(i)

def BFS(v):
    queue = deque([v])
    visited_bfs[v] = 1
    while queue:
        v = queue.popleft()
        # bfs.append(v)
        print(v, end=" ")

        for i in range(1,n+1):
            if visited_bfs[i] == 0  and graph[v][i] == 1:
                queue.append(i)
                visited_bfs[i] = 1

DFS(v)
print() # 에러 요소 발생으로 " " 형태에서 빈 프린트문으로 변경
BFS(v)

# Solved.ac Q.2667

#initialize
n = int(input())
graph = []
result = []
count = 0

# 제시된 그래프 받아오기
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 방향 정보
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# DFS 형식 풀이
def dfs(x, y):
    global count

    # 조건에 따라 반환조건 설정
    if x<0 or x>=n or y<0 or y>=n:
        return
    
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0

        # 4방향 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# 전체를 훑으면서 카운트 진행
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

# 최종 결과 정리
result.sort()

# 요구형태처럼 출력 진행
print(len(result))
for N in result:
    print(N)

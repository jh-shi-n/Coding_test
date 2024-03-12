## Solved.ac 12865 Question

# 가방 정보 세팅
n, k = map(int, input().split())

# 정보 입력할 공간 세팅
thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]


# 가방 내 넣을 물건 정보 세팅
for i in range(n):
    thing.append(list(map(int, input().split())))

# 세팅된 정보 기반 최적의 무게 찾기
for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])

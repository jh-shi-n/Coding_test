## Solved.ac Q 15649

# 값을 공백과 함께 받아오고 split
N, M = map(int, input().split())

# 값이 저장될 & 비교할 list 생성
list_select = []

def dfs():
    # 조건이 맞춰진 경우
    if len(list_select) == M:
        return print(' '.join(map(str, list_select)))

    # 값을 찾아가는 과정, 재귀과정 + 깊이우선탐색 과정을 통해 조건에 맞는 수열 출력
    for i in range(1, N+1):
        if i not in list_select:
            list_select.append(i)
            dfs()
            list_select.pop()

dfs()

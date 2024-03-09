## Solved.ac Question (1149)

# 집 갯수 입력
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

# 집 갯수별로 DP를 위한 테이블 생성 & 첫 번째 집은 기존과 동일하게
dp = [[0] * 3 for _ in range(n)]
dp[0] = house[0] 

# 타겟으로 하는 순번의 최솟값 가산방식을 통해 계산 진행
for i in range(1, n):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2]) + house[i][0]
    dp[i][1] += min(dp[i-1][0], dp[i-1][2]) + house[i][1]
    dp[i][2] += min(dp[i-1][0], dp[i-1][1]) + house[i][2]

# 최종 연산결과 출력
print(min(dp[n-1]))

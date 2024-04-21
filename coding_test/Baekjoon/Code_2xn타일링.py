### Backjoon (Solved.ac) Q. 11726

# 함수 작성
def count_num(n):
    dp = [0 for i in range(n)]

    # 타일 사이즈가 2 이하일 때 나올 수 있는 값을 미리 저장
    dp[0] = 1
    # 입력되는 값이 1일 때 발생할수 있는 오류를 방지하기 위해 if문 추가
    if len(dp) > 1:
        dp[1] = 2

    # n이 2 이상일 때 결과값은 n-1, n-2일때의 값을 더했을때와 동일
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2])  % 10007

    return dp[n-1]

n = int(input())
print(count_num(n))

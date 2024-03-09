## Solved.ac Silver (2579)

# 기본 세팅
n = int(input())
point = [int(input()) for _ in range(n)] # 계단 별 점수
dt =  [0] * n # 계산 결과 저장을 위한 배열

# 계단이 2개 혹은 그 이하일 경우
if len(point) <= 2:
    print(sum(point))

# 계단이 2개 이상일 경우
else:
    dt[0] = point[0] # 수동적용 - 첫번째 계단
    dt[1] = point[0] + point[1] # 수동적용 - 두번째 계단

    # 첫번째, 두번째 계단 확정 오름 이후 과정에 대해 점화식 적용
    for i in range(2,n) :
        dt[i] = max(dt[i-3]+point[i-1]+point[i], dt[i-2] + point[i])

    print(dt[-i])

## Solved.ac Q.1929

import math

## 함수 생성 + matn.sqrt() 적용을 통해 많은 숫자 없이도 소수 판별 가능하도록 함
def prime_check(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i == 0:
            return False

    # 모든 조건을 통과한 경우, True로 지정
    return True

## input 값 받아옴 + input된 숫자를 기반으로 range 설정 + for문 반복을 통해 체크
s,l = map(int, input().split())

for i in range(s, l+1):
    if prime_check(i) == True :
        print(i)

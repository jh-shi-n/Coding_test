#1차 시도 정확도 19.2/100
## 정확성 19.2/100
# 조합 생성(중복 비허용)
from itertools import combinations

#최소 1이상, 최대 3개의 숫자
#최소 3개의 숫자 합은 6이상이다

def prime_test(num):
    if num%2 == 0 or num%3 ==0:
        return False
    else:
        return True

#실제 풀이
def solution(nums):
    temp = []
    cnt = 0
    
    for i in combinations(nums,3):
        temp.append(sum(i))
    
    for j in range(len(temp)):
        if prime_test(temp[j]) == True:
            cnt += 1

    return cnt
    
##2차 시도 정확성 100/100
# 조합 생성(중복 비허용)
from itertools import combinations
import math

#최소 1이상, 최대 3개의 숫자
#최소 3개의 숫자 합은 6이상이다

def prime_test(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0 :
            return False    
    return True

#실제 풀이
def solution(nums):
    temp = []
    cnt = 0
    
    for i in combinations(nums,3):
        temp.append(sum(i))
    
    for j in range(len(temp)):
        if prime_test(temp[j]) == True:
            cnt += 1

    return cnt

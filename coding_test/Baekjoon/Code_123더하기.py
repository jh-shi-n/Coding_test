# 재귀함수 작성을 통해 반복적으로 값에 대한 비교 진행
def sum_number(x):
    if x==1:
      return 1
    elif x==2:
      return 2
    elif x==3:
      return 4
    else:
      return sum_number(x-1) + sum_number(x-2) + sum_number(x-3)

# 몇개의 값을 입력받을 것인지, 그리고 입력된 값마다 재귀함수에 입력하여 결과값 도출
N = int(input())
for _ in range(N):
    target = int(input())
    print(sum_number(target))

## Silver 4  _ Q 2839 (Solved.ac)

kg_sugar = int(input()) # 입력받는 설탕 무게
cnt = 0 # 가방숫자 Count 

while kg_sugar >= 0:
    if kg_sugar % 5 == 0: # 5의 배수로 최대한 나눠지는게 가장 설탕 가방을 적게 들수 있는 방법
        cnt += (kg_sugar // 5)
        print(cnt)
        break
    kg_sugar -= 3 # 5의 배수로 안 나눠지는 경우에 3키로 설탕 봉지를 하나 추가한다고 생각
    cnt += 1

else: # 제공되는 숫자가 조건에 부합하지 않는 경우
    print(-1)

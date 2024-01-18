#answer라는 빈 list 생성, n에 입력된 값들을 for문으로 한글자씩 확인해가면서 여러가지의 if문을 통과시킴
# if ~ answer에 들어가있는 값이 0이라면(없다면) 1
# if ~ answer의 끝(마지막으로 들어온 값)이 현재 반복문 순서의 값과 동일하다면 같은 값이 연속으로 붙어있다는 뜻 = like aa, bb // 붙어있기때문에 삭제
# 최종적으로 반복문이 전부 돌았을때 answer가 비어있다면 1 리턴, 값이 있다면 0 리턴

def solution(n):
    answer = []
    
    for i in n :
        if len(answer) == 0:
            answer.append(i)
            continue

        if answer[-1] == i:
            answer.pop()

        else:
            answer.append(i)

    if len(answer) == 0:
        return 1

    if len(answer) != 0:
        return 0

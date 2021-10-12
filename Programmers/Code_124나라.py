def solution(n):
    numlist = [4,1,2]
    stack = []

		#3으로 나누는 것으로 접근

    if n > 0:
        temp = n
        while temp // 3 >  0:
            if temp % 3 == 0:
                stack.append(temp % 3)
                temp = temp - 1

            else:
                stack.append(temp % 3)

            temp = temp//3

        if temp != 0:
            stack.append(temp)

    # 값이 거꾸로 저장되었기 때문에 거꾸로 불러오기
    answer = []
    for ii in stack[::-1]:
        if ii == 0:
            answer.append(str(numlist[ii]))
        elif ii == 1:
            answer.append(str(numlist[ii]))
        elif ii == 2:
            answer.append(str(numlist[ii]))

    return "".join(answer)

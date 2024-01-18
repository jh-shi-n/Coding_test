def solution(a, b):
    sum_list =[]
    
    for i in range(len(a)):
        temp = (a[i]*b[i])
        sum_list.append(temp)
    
    answer = sum(sum_list)
    return answer

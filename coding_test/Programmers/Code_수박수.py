def solution(n):
    
    keyword = '수박'
    
    if n % 2 == 1:
        answer = keyword * int(n/2) + keyword[0]
    
    else : 
        answer = keyword * int(n/2)
    
    
    return answer

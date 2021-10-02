#divmod와 int로 활용

def solution(n):
    nm = ""
    
    while n>=1:
        n, re = divmod(n, 3)
        nm += str(re)
        
    return int(nm, 3)

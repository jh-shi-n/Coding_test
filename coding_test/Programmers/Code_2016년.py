#일주일이 7일이라는 개념을 활용하여 나눠지도록 함

def solution(a, b):
    
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    answer = day[(sum(date[:a-1])+b-1)%7]
    
    return answer

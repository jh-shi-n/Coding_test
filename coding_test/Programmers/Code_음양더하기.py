def solution(absolutes, signs):
    
    for i in range(len(absolutes)):
        if signs[i] is False:
            absolutes[i] = (-absolutes[i])
        
        else:
            continue
        
    
    answer = sum(absolutes)
    return answer

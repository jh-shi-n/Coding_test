def solution(bridge_length, weight, truck_weights):
    
    second = 0 #기본 시간 0초
    bridge_in = [0] * bridge_length #다리 길이만큼 bridge_in 늘리기
      
    while len(bridge_in): # 지나가는동안 1초씩 추가
        second += 1
        bridge_in.pop(0)
        sum_bri_weights = sum(bridge_in)
        
        if truck_weights: 
            if  sum_bri_weights + truck_weights[0] <= weight:
                bridge_in.append(truck_weights.pop(0))    
            
            else:
                bridge_in.append(0)
        
    return second    

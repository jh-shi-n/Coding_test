def solution(numbers):
    set_nums = range(0,10)
    temp = []
    numbers.sort()
    
    for i in range(len(set_nums)):
        if set_nums[i] not in numbers:
            temp.append(set_nums[i])

    answer=sum(temp)
      
    
    return answer

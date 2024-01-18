participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

#1차시도 _ 작동자체는 OK, 하지만 효율성이 제로
def solution(participant, completion):
    for i in range(len(completion)):
        participant.remove(completion[i])
    
    answer = ''.join(participant)
    
    return answer
    
#2차시도 _ 효율성 향상을 위해 sort 및 zip, pop 추가
#sort를 통해 participant와 completion의 순서를 오름차순으로 변경
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

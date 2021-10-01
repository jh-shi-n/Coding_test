#1차 (쥬피터 노트북에서는 정상작동, 프로그래머스 콘솔창에서는 오류)
def del_anotherword(word):
    temp = ""
    for i in word:
        if ("0" <= i <= "9" or "a" <= i <= "z" or  i in "-_."):
            temp += i
    return temp

def solution(new_id):
    answer=""
    z = new_id.lower()
    z = del_anotherword(z)

    while '..' in z:
        z = z.replace("..",".")

    if z[0] == "." :
        z = z[1:]

    if z[(len(z)-1)] == "." :
        z = z[:-1]
    
    if z == "":
        z += "a"

    if len(z) >= 16:
        z = z[:15]
        if z[len(z)-1] == ".":
            z= z[:-1]

    if len(z) <= 2:
        for k in range(0,3):
            if len(z) == 3:
                break
            z += z[len(z)-1]
            
    answer += z
    
    return answer
  
  #2차시도 (이에 대해 오류가 발생하던 끝쪽 "." 찾는 코드를 strip 함수로 변경하면서 나머지 코드 중 끝자리를 제거하는 코드도 적당하게 수정)
  def del_anotherword(word):
    temp = ""
    for i in word:
        if ("0" <= i <= "9" or "a" <= i <= "z" or  i in "-_."):
            temp += i
    return temp

def solution(new_id):
    answer=""
    z = new_id.lower()
    z = del_anotherword(z)

    while '..' in z:
        z = z.replace("..",".")


    z = z.lstrip(".")
    z = z.rstrip(".")

    if z == "":
        z += "a"

    if len(z) >= 16:
        z = z[:15]
        if z[len(z)-1] == ".":
            z = z.rstrip(".")

    if len(z) <= 2:
        for k in range(0,3):
            if len(z) == 3:
                break
            z += z[len(z)-1]
            
    answer += z
    
    return answer

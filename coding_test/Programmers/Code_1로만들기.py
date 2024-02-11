## Solved.ac Silver Question (1463)

n = int(input()) # Input value
dt = [0] * (10**6 + 1) # Empty List

# Dynamic Programming 기반 문제 풀이
for i in range(2, n+1):
    dt[i] = dt[i-1] + 1 

    # 2의 배수 or 3의 배수일 때의 경우
    if i % 2 == 0:
        dt[i] = min(dt[i], dt[i//2] + 1)
    if i % 3 == 0:
        dt[i] = min(dt[i], dt[i//3] + 1)

print(dt[n])

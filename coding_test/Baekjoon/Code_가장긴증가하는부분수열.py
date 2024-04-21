# Backjoon (solved.ac) Q. 11053

# initial setting
num = int(input())
list_num = list(map(int, input().split()))
# for Dynamic Programming
dp = [1 for _ in range(num)]

for i in range(num):
    for j in range(i):
        if list_num[i] > list_num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

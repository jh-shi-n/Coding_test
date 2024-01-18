# A/B
a, b = map(int, input().split())
print(a / b)

#사파리월드
N,M = map(int, input().split())
print(abs(N-M))

#1312 소수
# 런타임에러
# A,B,N = map(int, input().split())
# temp = str(A/B)[2:]
# print(int(temp[N-1]))
    
A,B,N=map(int, input().split())
A%=B
for i in range(N-1):
    A=(A*10) % B
    
print((A*10) // B)

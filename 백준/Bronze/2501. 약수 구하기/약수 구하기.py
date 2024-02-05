N,K = map(int,input().split())

# 약수 리스트 생성
divisor_li = []
for i in range(1,N+1):
    if N % i == 0:
        divisor_li.append(i)

# K번째로 작은 약수 출력
if len(divisor_li) > K-1:
    print(divisor_li[K-1])
else:
    print(0)

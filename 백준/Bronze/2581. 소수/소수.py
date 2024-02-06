M = int(input())
N = int(input())

prime_num_li = []
for i in range(M,N+1):
    divisor_li = []
    for j in range(1,i+1): 
        if i % j == 0: # 약수를 divisior_li에 추가
            divisor_li.append(j)
    if len(divisor_li) == 2: # 소수라면(약수가 2개라면)
        prime_num_li.append(i)


if len(prime_num_li) != 0:
    print(sum(prime_num_li))
    print(min(prime_num_li))
else:
    print(-1)
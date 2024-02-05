N = int(input())
num_list = map(int,input().split())

# 소수 : 약수가 1과 자기자신만 존재
prime_num_li = []
for num in num_list:
    divisor_len = len([i for i in range(1,num+1) if num % i == 0])
    if divisor_len == 2: # 소수이면
        prime_num_li.append(num)

print(len(prime_num_li))
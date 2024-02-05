while True:
    n = int(input())
    if n == -1:
        break

    # 약수 리스트 생성
    divisor_li = [i for i in range(1,n+1) if n % i == 0]
    divisor_li.remove(n)
    # 약수들의 합
    divisor_sum = sum(divisor_li)

    if divisor_sum != n: # 완전수가 아니면
        print(f'{n} is NOT perfect.')
    else: # 완전수이면
        print(n, '=', end = ' ')
        for j in range(len(divisor_li)):
            if j == len(divisor_li) -1:
                print(f'{divisor_li[j]}', end=' ')
            else:
                print(f'{divisor_li[j]}', '+', end=' ')
from itertools import combinations
def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False # 소수아니면 False
    return True # 소수면 True

def solution(nums):
    comb = combinations(nums, 3) # 3가지 선택하는 조합
    comb_list = [sum(c) for c in comb] # 선택된 조합의 합
    prime_num = sum(check_prime(comb) for comb in comb_list)
    return prime_num

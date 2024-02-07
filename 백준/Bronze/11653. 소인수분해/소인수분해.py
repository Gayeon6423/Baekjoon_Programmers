import math

def get_prime_factors(N):
    prime_factors = []
    
    # Divide N by 2 until it becomes odd
    while N % 2 == 0:
        prime_factors.append(2)
        N //= 2

    # Divide N by odd numbers starting from 3
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        while N % i == 0:
            prime_factors.append(i)
            N //= i

    # If N is a prime number greater than 2
    if N > 2:
        prime_factors.append(N)

    return prime_factors

# Input
N = int(input())

# Get prime factors
prime_factor_list = get_prime_factors(N)

# Output
for factor in prime_factor_list:
    print(factor)

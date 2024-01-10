import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

max = 0
for each in list(permutations(A)):
    ans = 0
    for i in range(N-1):
        ans += abs(each[i] - each[i+1])
    if ans > max : 
        max = ans

print(max)
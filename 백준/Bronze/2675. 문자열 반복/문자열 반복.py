T = int(input())

for _ in range(T):
    R, S = input().split()
    for word in S:
        print(word * int(R), end='')
    print()


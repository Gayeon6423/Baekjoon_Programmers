side = sorted(map(int,input().split()))

# 삼각형 조건 : 가장 큰 변의 길이 < 남은 두 변 길이의 합
# 변의 길이를 줄이는 것만 가능
if side[0] + side[1] > side[2]: # 삼각형의 조건에 부합한다면
    # 둘레 그대로 출력
    print(sum(side))
else: # 삼각형의 조건에 부합하지 않는다면
    # 가장 큰 값을 다른 숫자의 합보다 1만큼 작게 조절
    side[2] = side[0] + side[1] - 1
    print(sum(side))
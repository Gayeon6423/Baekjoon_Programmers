while True:
    a,b,c = map(int,input().split())
    side = sorted([a,b,c]) # 오름차순 정렬
    if side[0]==0 and side[1]==0 and side[2]==0:
        break
    elif (side[0] == side[1] == side[2]):
        print('Equilateral')
    elif (side[0] + side[1] > side[2]) and (side[0]==side[1]!=side[2] or side[0]==side[2]!=side[1] or side[1]==side[2]!=side[0]):
        print('Isosceles')
    elif (side[0] + side[1] > side[2]) and (side[0]!=side[1]!=side[2]):
        print('Scalene')
    elif (side[0] + side[1] <= side[2]):
        print('Invalid')

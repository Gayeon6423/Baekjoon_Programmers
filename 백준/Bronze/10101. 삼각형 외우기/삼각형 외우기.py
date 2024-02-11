angle_li = [int(input()) for _ in range(3)]

if angle_li[0] == angle_li[1] == angle_li[2]:
    print('Equilateral')
elif (sum(angle_li) == 180) and ((angle_li[0] == angle_li[1]) or (angle_li[0] == angle_li[2]) or (angle_li[1] == angle_li[2])):
    print('Isosceles')
elif (sum(angle_li) == 180) and (angle_li[0] != angle_li[1] != angle_li[2]):
    print('Scalene')
elif (sum(angle_li) != 180):
    print('Error')
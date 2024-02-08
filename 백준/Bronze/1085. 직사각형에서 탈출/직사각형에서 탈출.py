x,y,w,h = map(int, input().split())
# 경계 까지의 거리 : 현재 x좌표, 현재 y좌표, 오른쪽 꼭짓점과 현재 좌표의 차이
distance_li = [x,y,w-x,h-y]
print(min(distance_li))
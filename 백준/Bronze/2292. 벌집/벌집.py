N = int(input())

room_num = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while N > room_num : # 방의 수보다 입력값이 클 때까지
    room_num += 6 * cnt  # 벌집의 개수가 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)
def solution(name):
    answer = 0
    length = len(name)
    updown_move = 0
    leftright_move = 0
    # 상하 이동 최소 횟수
    for char in name:
        up_distance = ord(char) - ord('A') # 조이스틱 위로 이동
        down_distance = ord('Z') - ord(char) + 1 # 조이스틱 아래로 이동
        updown_move += min(up_distance,down_distance)
    
    
    # 좌우 이동 최소 횟수 계산
    min_leftright_move = length - 1
    for index in range(length):
        next_index = index + 1
        while next_index < length and name[next_index] == 'A': # 다음 문자가 'A'일때
            next_index += 1
        min_leftright_move  = min(min_leftright_move, # 우측으로만 이동
                                  2 * index + length - next_index,
                                  index + 2 * (length - next_index))

    leftright_move += min_leftright_move
    answer = updown_move + leftright_move

    return answer
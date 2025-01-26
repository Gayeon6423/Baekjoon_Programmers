def solution(name):
    ans = 0
    length = len(name)
    # 알파벳 변경 횟수
    up_down_move = 0
    # 커서 이동 횟수
    left_right_move = length - 1

    for index, spell in enumerate(name):
        # 알파벳 변경(위로 이동)
        up = ord(spell) - ord('A')
        # 알파벳 변경(아래로 이동)
        down = ord('Z') - ord(spell) + 1
        up_down_move += min(up,down)
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next_index = index + 1
        while next_index < length and name[next_index] == 'A':
            next_index += 1
        left_right_move = min([left_right_move, # 이전 커서 이동 값(->)
                            2*index + length - next_index, # 연속된 A의 왼쪽 시작(->,<-,<-)
                            index + 2*(length - next_index)  # 연속된 A의 오른쪽 시작(<-,->,->)
                                        ])
    ans = up_down_move + left_right_move
    return ans
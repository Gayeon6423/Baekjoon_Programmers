def solution(nums):
    answer = 0    

    type_num = len(set(nums))
    select_num = int(len(nums)/2)

    if select_num < type_num:
        # 선택하는 폰켓못 수가 폰켓못 타입 수보다 많으면
        answer = select_num # 종류 = 선택 수
    else:
        # 선택하는 폰켓몬 수가 폰켓못 타입 수보다 적으면 
        answer = type_num # 종류 = 타입 수

    return answer
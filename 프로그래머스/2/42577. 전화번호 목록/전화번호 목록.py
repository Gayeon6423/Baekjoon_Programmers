## hash map 생성
def solution(phone_bank):
    hash_map = {}
    for phone in phone_bank:
        hash_map[phone] = 1
    # 접두어가 hash map에 존재하는지 찾기
    for phone in phone_bank:
        arr = ""
        for p in phone:
            arr += p
            # 접두어가 본인 자체이면 제외
            if arr in hash_map and arr != phone:
                return False
    return True

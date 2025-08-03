def solution(genres, plays):
    answer = []  # 선택된 노래의 인덱스를 담을 리스트

    dic1 = {}  # 장르별 노래 정보를 담을 딕셔너리 (장르별로 인덱스와 재생 횟수를 저장)
    dic2 = {}  # 장르별 총 재생 횟수를 담을 딕셔너리

    # 각 노래의 장르와 재생 횟수를 순서대로 처리
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:  # dic1에 해당 장르가 없다면
            dic1[genre] = [(index, play)]  # 새로운 장르를 생성하고 (인덱스, 재생 횟수) 정보를 리스트로 저장
        else:  # 이미 dic1에 해당 장르가 있다면
            dic1[genre].append((index, play))  # 해당 장르에 (인덱스, 재생 횟수) 정보를 추가

        if genre not in dic2:  # dic2에 해당 장르가 없다면
            dic2[genre] = play  # 새로운 장르를 생성하고 재생 횟수를 저장
        else:
            dic2[genre] += play  # 이미 dic2에 해당 장르가 있다면 재생 횟수를 누적하여 업데이트

    # 재생 횟수를 기준으로 장르를 내림차순으로 정렬하여 처리
    for (genre, total_play) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        # 해당 장르의 노래들을 재생 횟수를 기준으로 내림차순으로 정렬하고 상위 2개 노래 선택
        for (index, play) in sorted(dic1[genre], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(index)  # 선택된 노래의 인덱스를 answer 리스트에 추가

    return answer  # 선택된 노래의 인덱스 리스트 반환
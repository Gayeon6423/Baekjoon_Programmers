# 모든 음식의 지수 >= K로 만들기
# 섞은 음식 = 지수 가장 낮은 음식 + (2* 지수 두번째로 낮은 음식)
# 힙(우선순위 큐 알고리즘)을 통해 해결
# heappush(heap,item) : item을 heap에 추가
# heappop(heap) : heap에서 가장 작은 항목 팝하고 반환, 비어있으면 IndexError
# heapify(x) : 리스트 x를 선형 시간으로 제자리에서 힙으로 변환

## 풀이 과정
# 1. 최조의 scoville 리스트를 힙으로 변환 -> 오름차순 정렬(최소힙)
# 2. 정렬한 리스트의 0번째 값과 1번째 값을 이용하여 섞었을 때 스코필 지수 계산
# 3. 0번째, 1번째 값을 heappop을 이용해 pop
# 4. 계산된 새로운 스코빌 지수를 heappush 를 이용해 push

import heapq
def solution(scoville, K):
    ans = 0
    mix_scoville = 0
    heapq.heapify(scoville)
    # 최조 리스트에서 힙 정렬 -> 최소힙
    while scoville[0] < K:
        # 가장 작은 스코빌 지수가 K랑 같아질 때까지 반복
        if (len(scoville) < 2):
            # 스코빌 지수가 하나 남았을 때 -1 반환
            return -1
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mix_scoville)
        ans += 1
    return ans    
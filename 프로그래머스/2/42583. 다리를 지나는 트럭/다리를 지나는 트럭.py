from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0]*bridge_length) # 현재 다리 위에 있는 트럭의 리스트(큐)
    current_weight = 0 # 현재 다리 위 무게
    while len(truck_weights) > 0: # truck_weights가 차있을때까지 반복
        time = time + 1
        current_weight = current_weight - bridge.popleft()
        if current_weight + truck_weights[0] <= weight:
            current_weight = current_weight + truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    time = time + bridge_length
    return time
    
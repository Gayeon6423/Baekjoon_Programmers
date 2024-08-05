def solution(brown, yellow):
    total_tiles = brown + yellow
    for height in range(1, yellow + 1):
        if yellow % height == 0:
            width = yellow // height
            if (width + 2) * (height + 2) == total_tiles:
                return [width + 2, height + 2]
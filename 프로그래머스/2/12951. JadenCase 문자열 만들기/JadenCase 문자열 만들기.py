def solution(s):
    words = s.split(" ")
    tmp1 = []

    for word in words:
        tmp2 = []
        for i in range(len(word)):
            if i == 0:
                tmp2.append(word[i].upper())
            else:
                tmp2.append(word[i].lower())
        tmp1.append("".join(tmp2))
    return " ".join(tmp1)
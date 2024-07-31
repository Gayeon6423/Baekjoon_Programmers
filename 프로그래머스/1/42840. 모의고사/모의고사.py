def solution(answers):
    first = [i for i in range(1,6)] * 2000
    second = [2,1,2,3,2,4,2,5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    frist_answer = sum(1 for x,y in zip(answers, first) if x==y)
    second_answer = sum(1 for x,y in zip(answers,second) if x==y)
    third_answer = sum(1 for x,y in zip(answers,third) if x==y)

    all_answer_dict = {1:frist_answer,2:second_answer,3:third_answer}
    max_value = max(all_answer_dict.values())
    max_key = sorted([key for key,value in all_answer_dict.items() if value==max_value])
    return max_key 

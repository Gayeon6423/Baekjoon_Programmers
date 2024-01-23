input_chess_list = list(map(int, input().split()))
answer_chess_list = [1,1,2,2,2,8]
output_chess_list = []
       
for i in range(len(answer_chess_list)):
    if answer_chess_list[i] == input_chess_list[i]:
        output_chess_list.append(0)
    else:
        output_chess_list.append(answer_chess_list[i] - input_chess_list[i])

for i in output_chess_list:
    print(i, end=' ')
T = int(input())
change_dict = {'Quarter':25,'Dime':10,'Nickel':5,'Penny':1}

for _ in range(T):
    price = int(input())
    change_num_dict = {'Quarter':0,'Dime':0,'Nickel':0,'Penny':0}
    for change_name, change in change_dict.items():
        # 사용한 동전의 개수는 가격을 거스름돈으로 나눈 몫
        change_num_dict[change_name] += price // change
        # 남은 거스름돈은 가격을 거스름돈으로 나눈 나머지로 업데이트
        price = price % change
    print(change_num_dict['Quarter'], change_num_dict['Dime'],change_num_dict['Nickel'],change_num_dict['Penny'])


S = input()
num_dict = {'2':['A','B','C'],
            '3':['D','E','F'],
            '4':['G','H','I'],
            '5':['J','K','L'],
            '6':['M','N','O'],
            '7':['P','Q','R','S'],
            '8':['T','U','V'],
            '9':['W','X','Y','Z']}

time = 0
for word in S:
    for num, alp in num_dict.items():
        if word in alp:
            time = time + int(num) + 1
print(time)        


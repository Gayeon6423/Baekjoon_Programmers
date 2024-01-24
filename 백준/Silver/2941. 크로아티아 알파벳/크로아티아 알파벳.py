croatia = input()
croatia_dict = {'c=':'c', 'c-':'c','dz=':'d','d-':'d',
                'lj':'l','nj':'n','s=':'s','z=':'z'}
for key, value in croatia_dict.items():
    if key in croatia:
        croatia = croatia.replace(key, croatia_dict[key])
print(len(croatia))
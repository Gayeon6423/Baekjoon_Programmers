student_li = [int(i) for i in range(1,31)]
submit_li = []

for _ in range(28):
    n = int(input())
    submit_li.append(n)

for i in submit_li:
    student_li.remove(i)

student_li.sort()
for i in student_li:
    print(i)
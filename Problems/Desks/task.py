# put your python code here
students_num = list()
students_num.append(int(input()))
students_num.append(int(input()))
students_num.append(int(input()))
desks = 0
for eff in students_num:
    desks += (eff // 2) + (eff % 2)
print(desks)

name_list = input("이름을 나열하시오(구분자 : ','): ").split(',')
count_kim = 0
count_lee = 0
count = 0
for i in name_list:
    if '김' in i:
        count_kim += 1
    elif '이' in i:
        count_lee += 1
    if i=='이재영':
        count += 1
print('1. 김씨 :',count_kim,'명, 이씨 :',count_lee,'명' )
print('2. 이재영 :',count,'명')
new_name_list = list(set(name_list))
print('3.', end=' ')
for i in new_name_list:
    print(i, end=' ')
print()
print('4.', end=' ')
new_name_list.sort()
for i in new_name_list:
    print(i, end=' ')
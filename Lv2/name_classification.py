# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.
#
# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌
#
# 1. 김씨와 이씨는 각각 몇 명 인가요?
# 2. "이재영"이란 이름이 몇 번 반복되나요?
# 3. 중복을 제거한 이름을 출력하세요.
# 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

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
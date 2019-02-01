# 문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.
#
# 입력 예시: aaabbcccccca
#
# 출력 예시: a3b2c6a1

str = input('문자열을 입력하시오 :')
result = []
result.append(str[0])
count = 1
for i in range(len(str)-1):
    if str[i] == str[i+1]:
        count += 1
    else:
        result.append(count)
        result.append(str[i+1])
        count =1
result.append(count)
for i in result:
    print(i, end ='')
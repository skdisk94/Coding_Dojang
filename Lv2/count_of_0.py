# N!의 정의는 다음과 같습니다.
#
# N! = 1 * 2 * 3 * 4 ... N
# 이때 N!를 정수로 변환 해 뒤에서 부터 연속되는 0의 갯수를 구하세요.
#
# 예) f(12) -> 2 # 12!은 479001600 f(25) -> 6 # 25!은 15511210043330985984000000

def N(n):
    if n == 1 :
        return 1
    else:
        return N(n-1)*n

n = int(input('숫자를 입력하시오 :'))
result = N(n)
count = 0
i = -1
while True:
    if str(result)[i] == '0':
        count+=1
        i-=1
    else:
        break
print(result,end=' -> ')
print(count)
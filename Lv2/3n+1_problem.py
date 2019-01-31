def p(n):
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    return int(n)
i, j = map(int, input('min num, max num의 값을 입력하시오: ').split())
max_cycle = 0
for n in range(i,j):
    pro=[]
    pro.append(n)
    while n != 1:
        n = p(n)
        pro.append(n)
    if max_cycle < len(pro):
        max_cycle = len(pro)
print(i, j, max_cycle)
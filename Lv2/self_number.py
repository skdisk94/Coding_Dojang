def d(a):
    num = str(a)
    generator = 0
    for i in range(len(num)):
        generator += int(num[i])
    generator += a
    return  generator

generator_num=list(range(1,5001))
for i in range(1,5001) :
    if d(i) in generator_num :
        generator_num.remove(d(i))

print(generator_num)
print(sum(generator_num))
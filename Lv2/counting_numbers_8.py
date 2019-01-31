count = 0
for i in range(10001):
    num = str(i)
    for k in num:
        if '8' in k:
            count +=1
print(count)

# print(str(list(range(1,10001))).count('8'))
s=[1, 3, 4, 8, 13, 17, 20]
min_d = s[1] - s[0]
for i in range(len(s)-1):
    d = s[i+1]-s[i]
    if d < min_d:
        a = s[i]
        b = s[i+1]
        min_d = d
print('({0},{1})'.format(a,b))
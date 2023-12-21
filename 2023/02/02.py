'''
# 1
res = 0
with open('2.txt') as f:
    i = 0
    for game in f:
        i += 1
        x = map(lambda x: x.strip(), game.strip('\n').split(':')[1].replace(';', ',').split(','))
        for p in x:
            num, col = p.split()
            if col == 'red' and int(num) > 12:
                break
            elif col == 'green' and int(num) > 13:
                break
            elif col == 'blue' and int(num) > 14:
                break
        else:
            res += i
print(res)
'''

# 2
res = 0
with open('2.txt') as f:
# with open('a') as f:
    for game in f:
        x = map(lambda x: x.strip(), game.strip('\n').split(':')[1].replace(';', ',').split(','))
        # print(list(x))
        min_red, min_green, min_blue = 0, 0, 0
        for p in x:
            num, col = p.split()
            num = int(num)
            if col == 'red':
                min_red = max(min_red, num)
            elif col == 'green':
                min_green = max(min_green, num)
            elif col == 'blue':
                min_blue = max(min_blue, num)
        res += min_red*min_green*min_blue
print(res)

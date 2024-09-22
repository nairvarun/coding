import string

alphabets = (string.ascii_uppercase)
numbers = (i for i in range(1, 27))
value = dict(zip(alphabets, numbers))

names = []
with open('./p022_names.txt', 'r') as file:
    for line in file:
        names += line.replace('"', '').split(',')
names.sort()
enumerated_names = enumerate(names, 1)

def get_score(x):
    rank = x[0]
    worth = sum(map(lambda x: value[x], x[1]))
    return rank * worth

print(sum(map(get_score, enumerated_names)))


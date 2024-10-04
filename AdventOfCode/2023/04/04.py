'''
# 1
# f = open('a.txt')
f = open('4.txt')

res = 0
for line in f.readlines():
    score = -1
    winning_nums, our_nums = ((int(num) for num in i.strip().split()) for i in line.split(':')[1].split('|'))
    winning_set = set(winning_nums)
    for num in our_nums:
        if num in winning_set:
            score += 1
    res += int(2**score)

print(res)

f.close()
'''

# 2
# f = open('a.txt')
f = open('4.txt')

num_cards = len(f.readlines())
f.seek(0)

cards = {i: 1 for i in range(1, num_cards+1)}

for curr_card, line in enumerate(f.readlines(), start=1):
    score = 0
    winning_nums, our_nums = ((int(num) for num in i.strip().split()) for i in line.split(':')[1].split('|'))
    winning_set = set(winning_nums)

    for num in our_nums:
        if num in winning_set:
            score += 1

    next_card = curr_card + 1
    for card in range(next_card, min(num_cards+1, next_card+score)):
        cards[card] = cards[card]+(1 * cards[curr_card])

print(sum(cards.values()))

f.close()

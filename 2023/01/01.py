'''
# 1
sum = 0
with open('1.txt') as f:
    for line in f:
        for i in line:
            if i.isdigit():
                sum += int(i)*10
                break
        for i in line[::-1]:
            if i.isdigit():
                sum += int(i)
                break
print(sum)
'''

# 2
sum = 0
digit = None
with open('1.txt') as f:
    for line in f:
        found_first_digit = False
        found_digit = False
        for idx, i in enumerate(line):
            if i.isdigit():
                digit = i
                found_digit = True
            elif line[idx:idx+3] == 'one':
                digit = 1
                found_digit = True
            elif line[idx:idx+3] == 'two':
                digit = 2
                found_digit = True
            elif line[idx:idx+5] == 'three':
                digit = 3
                found_digit = True
            elif line[idx:idx+4] == 'four':
                digit = 4
                found_digit = True
            elif line[idx:idx+4] == 'five':
                digit = 5
                found_digit = True
            elif line[idx:idx+3] == 'six':
                digit = 6
                found_digit = True
            elif line[idx:idx+5] == 'seven':
                digit = 7
                found_digit = True
            elif line[idx:idx+5] == 'eight':
                digit = 8
                found_digit = True
            elif line[idx:idx+4] == 'nine':
                digit = 9
                found_digit = True

            if found_digit and not found_first_digit:
                sum += int(digit)*10
                found_first_digit = True
        else:
            sum += int(digit)
print(sum)

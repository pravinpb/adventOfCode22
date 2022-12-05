#fetching the input (iinstructions only)

f = open('input.txt','r')
instructions = []
for i in f:
    instructions.append(i)
#formating the input

instructions = [l.replace('\n','') for l in instructions]
instructions = [[int(l.split(' ')[1]),int(l.split(' ')[3]),int(l.split(' ')[5])] for l in instructions]

# [N]     [Q]         [N]            
# [R]     [F] [Q]     [G] [M]        
# [J]     [Z] [T]     [R] [H] [J]    
# [T] [H] [G] [R]     [B] [N] [T]    
# [Z] [J] [J] [G] [F] [Z] [S] [M]    
# [B] [N] [N] [N] [Q] [W] [L] [Q] [S]
# [D] [S] [R] [V] [T] [C] [C] [N] [G]
# [F] [R] [C] [F] [L] [Q] [F] [D] [P]
#  1   2   3   4   5   6   7   8   9 

# list of supplies given

supplies = [
    [],list('FDBZTJRN'),list('RSNJH'),
    list('CRNJGZFQ'),list('FVNGRTQ'),list('LTQF'),
    list('QCWZBRGN'),list('FCLSNHM'),list('DNQMTJ'),
    list('PGS')
]

# ------------------------------------------------------------------------------------------------------------------- #

'''Task 1'''

for instruction in instructions:
    for count in range(instruction[0]):
        supplies[instruction[2]-1].append(supplies[instruction[1]-1].pop())

output = ''
for i in supplies:
    output += i[-1]
print(output)

# ------------------------------------------------------------------------------------------------------------------- #

'''Task 2'''

for instruction in instructions:
    supplies[instruction[2]] = supplies[instruction[2]]+supplies[instruction[1]][-instruction[0]:]
    for count in range(instruction[0]):
        supplies[instruction[1]].pop()

output = ''
for i in supplies:
    if len(i)>0:
        output += i[-1]
print(output)

# ------------------------------------------------------------------------------------------------------------------- #
# fetching the inputs

f = open('input.txt','r')

# formating the inputs
all_rucksacks = []
for rucksack in f:
    all_rucksacks.append(rucksack)
all_rucksacks = [rucksack.replace('\n','') for rucksack in all_rucksacks]

# Alphabets for the score calculation
alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


'''Task 1'''

score1 = 0
for rucksack in all_rucksacks:

    # finding the mid value
    mid = len(rucksack)//2
    
    # seperating into two seperate lists
    left,right = rucksack[:mid],rucksack[mid:]
    
    # checking and increasing the score if common item exist
    for item in left:
        if item in right:
            score1 += alp.index(item)+1
            break

# ----------------------------------------------------------------------------- #

'''Task 2'''

score2 = 0
grouped = []

# seperating as a group of 3
for i in range(0,len(all_rucksacks), 3):
    grouped.append(all_rucksacks[i:i+3])

for input in grouped:
    # asigning each item into different variables
    a,b,c = input

    # checking and increasing the score if common item exist
    for item in a:
        if item in b and item in c:
            score2 += alp.index(item)+1
            break

# ----------------------------------------------------------------------------- #

print(f'Score-1 :{score1}')
print(f'Score-2 :{score2}')
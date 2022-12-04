# Fetching the input
f = open('input.txt','r')


# Formating the input
lis = []
for i in f:
    lis.append(i)
lis = [work.replace('\n','') for work in lis]


'''Task 1'''

score1 = 0
for section in lis:

    # seperating the ranges
    range1 , range2 = section.split(',')
    
    # converting it into range from string
    range1 = list(range(int(range1.split('-')[0]),int(range1.split('-')[1])+1))
    range2 = list(range(int(range2.split('-')[0]),int(range2.split('-')[1])+1))

    # converting it into sets
    set1 = set(range1)
    set2 = set(range2)

    # checking for the engulfed items
    if set1.union(set2) == set1 or set2.union(set1) == set2:
        score1 += 1

print(f'Score1 :{score1}')

# ----------------------------------------------------------------------------- #

'''Task 2'''

score2 = 0

for section in lis:

    # seperating the ranges
    range1 , range2 = section.split(',')

    # converting it into range from string
    range1 = list(range(int(range1.split('-')[0]),int(range1.split('-')[1])+1))
    range2 = list(range(int(range2.split('-')[0]),int(range2.split('-')[1])+1))

    # converting it into sets
    set1 = set(range1)
    set2 = set(range2)

    # checking for the engulfed items
    if set1.intersection(set2):
        score2 +=1

print(f'score2 :{score2}')

# ----------------------------------------------------------------------------- #


# Fetching the input
f = open('input.txt','r')
for document in f:
    d = document

# ------------------------------------------------------------- #

'''Task 1'''

character_index_1 = 0

for i in range(len(d) - 4):
    if len(set(d[i:i+4])) == 4:
        character_index_1 = i+4
        break

print(character_index_1)

# ------------------------------------------------------------- #

'''Task 2'''

character_index_1 = 0

for i in range(len(d) - 14):
    if len(set(d[i:i+14])) == 14:
        character_index_2 = i+14
        break

print(character_index_2)

# ------------------------------------------------------------- #
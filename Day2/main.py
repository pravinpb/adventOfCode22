#fetching the inputs 
f = open('input.txt','r')

# formating the inputs
player_inputs = []
for player_input in f:
    player_inputs.append(player_input)

player_inputs = [player_input.replace('\n','') for player_input in player_inputs]

'''Task 1'''

#Scores for task 1
scores_of_round_1 = {
    'A X' : 4,
    'B X' : 1,
    'C X' : 7,
    'A Y' : 8,
    'B Y' : 5,
    'C Y' : 2,
    'A Z' : 3,
    'B Z' : 9,
    'C Z' : 6
    }
# Itterating the each turn and adding the score of each turn.

scores_of_each_round_task1 = [scores_of_round_1[turn] for turn in player_inputs]
print(f'ScoreOfRound1 :{sum(scores_of_each_round_task1)}')

# ----------------------------------------------------------------------------- #


'''Task 2'''

scores_of_round_2 = {
    'A X' : 3,
    'B X' : 1,
    'C X' : 2,
    'A Y' : 4,
    'B Y' : 5,
    'C Y' : 6,
    'A Z' : 8,
    'B Z' : 9,
    'C Z' : 7
    }
# Itterating the each turn and adding the score of each turn.

scores_of_each_round_task2 = [scores_of_round_2[turn] for turn in player_inputs]
print(f'ScoreOfRound2 :{sum(scores_of_each_round_task2)}')

# ----------------------------------------------------------------------------- #

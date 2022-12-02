#Reading the text file
f = open('input.txt','r')


'''Task1'''

#putting the individual calories into a list
individual_calories = []
for calories in f:
    individual_calories.append(calories)

#formating the list for processing

#replacing "\n" with an empty string
individual_calories = [calorie.replace('\n','') for calorie in individual_calories]
individual_calories_formated = []

#converting the string to integers
for calorie in individual_calories:
    if calorie != '':
        individual_calories_formated.append(int(calorie))
    else:
        individual_calories_formated.append(calorie)



#seperating the calories of an individual elf into seperate lists
total_individual_calories = []
calories_in_single_elf = []
for calorie in individual_calories_formated:
    if calorie == '':
        if len(calories_in_single_elf)!=0:
            total_individual_calories.append(calories_in_single_elf)
        calories_in_single_elf = []
    else:
        calories_in_single_elf.append(calorie)

#total calorie in each elf
total_individual_calories = [sum(calorie_in_each_elf) for calorie_in_each_elf in total_individual_calories]




'''Task 2'''

#sorting the total calories in decending order
list.sort(total_individual_calories)
total_individual_calories.reverse()

#sum of calories in top 3 elves containing more calories
print(sum(total_individual_calories[:3]))
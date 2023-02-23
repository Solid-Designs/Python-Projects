# IMPORTANT: THIS PROGRAM IS DUMB, SO I AM GOING TO MAKE A NEW ONE
# INSTEAD OF CHOOSING THE MEET FOR EACH WEEK. I'll MAKE A PROGRAM THAT JUST RANDOMIZES FROM A BIG LIST WITH ONE BUTTON CLICK
import random

recipes = {
    'Chicken':['Alfredo', 'Cajun Pasta', 'Riggies', 'Parm', 'Quesadillas'],
    'Beef':['Tacos', 'Burgers', 'Taco bowls', 'Spaghetti'], 
    'Pork':['Pork Steaks', 'Pork Chops', 'Ham'],
    'Fish': ['Tuna', 'Sticks', 'Shrimp']}

main_menu = '''
1. Chicken
2. Beef
3. Pork
4. Fish
5. Quit Program'''

meal_plan = []

def get_protein():
    duplicate = False

    print('Welcome to the meal plan generator.\nSelect Your meat.', main_menu)
    
    while True:
        user_answer = str(input())
        if user_answer == '1' and len(meal_plan) < 8:
            #Grab a random recipe within the length of the list, then append to meal plan list
            meal_plan.append(randomize_recipe('Chicken'))
            check_duplicates()
        elif user_answer == '2':
            randomize_recipe('Beef')
        elif user_answer == '3':
            randomize_recipe('Pork')
        elif user_answer == '4':
            randomize_recipe('Fish')
        elif user_answer == '5':
            break
        else:
            print('Please input a number that matches a menu choice: ')

    print(meal_plan)

def randomize_recipe(protein):
    return(recipes[protein][random.randrange(len(recipes[protein]))])

def check_duplicates():
    if len(meal_plan) != len(set(meal_plan)):
        return True

get_protein()



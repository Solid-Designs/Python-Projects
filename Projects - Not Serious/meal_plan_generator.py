# Create an app that will pull from a database of recipes 
# Then generate a meal plan automatically when the user selects the prompt
# Or the user can quit out of the program
# Output the meal plan in a text file, and then email it
# * Eventually the user will be able to use it as a CRUD app to make edits to the recipes
import random

recipes = ['Chicken Riggies', 'Taco Bowls', 'Burgers', 'Cajun Chicken Pasta',
'Pork Steaks', 'Chicken and Dumplings', 'Salads', 'Sloppy Joes', 'Tuna', 'Rotel Dip', 
'Hot Pockets', 'Hot Dogs', 'Fajitas', 'Chicken Tenders and Fries']


def display_menu_screen():
    print('Welcome to the meal plan generator.')
    while True:
        print('1. Generate meal plan\n2. Exit the program')
        user_input = str(input('Select a corresponding menu item: '))
        
        if(user_input == '1'):
            print('Generating...')
            export_plan(create_meal_plan())
            break
        elif(user_input == '2'):
            break
        else:
            print('That is an invalid option. Try again')

def create_meal_plan():
    # 1. Randomly pull 8 meals from the recipes list without duplicates
    # 2. Then place into another list to then be exported into a txt file
    meal_plan = []
    # Get random numbers within the length of the recipe list and grab 8 of them. WITH NO DUPLICATES due to using "random.sample()"
    random_integers = random.sample(range(len(recipes)), 8)

    # 1. Use the numbers in the random_integers list to then iterate through the recipes list
    # 2. Then place the corresponding list item into the meal_plan list so there are no duplicate meals###
    for number in random_integers:
        meal_plan.append(recipes[number])
        if len(meal_plan) == 8:
            break

    print(meal_plan)
    return(str(meal_plan))

# Export the plan into a text file
# ***Tomorrow*** Make a folder for the meal plans and make the file names the current month
def export_plan(generated_plan):
    with open('test_plan.txt', 'w') as f:
        f.write(generated_plan)
        

display_menu_screen()


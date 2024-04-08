# presentation layer

import requests
import textwrap

# displays title of program
def show_title():
    print("My Recipe Program")
    print()


# displays menu
def show_menu():
    print("COMMAND MENU")
    print("1 - List all categories")
    print("2 - List all meals for categories")
    print("3 - Search meal by name")
    print("4 - Get a random meal")
    print("5 - List all areas")
    print("6 - List all meals for an area")
    print("7 - Display menu")
    print("0 - Exit the application")
    print()


def list_categories():
    # get return type
    categories = requests.get_categories()

    # handels exception if requests.get_categories() returns None
    if categories is not None:
        print("CATEGORIES")
        # for loop that assigns how over many indexes there are for the length of categories
        for i in range(len(categories)):
            category = categories[i]
            # prints each category by index
            print("  " + category.get_category())
        print()
    else:
        print("\nTechnical difficulties, please try again later\n")


def list_meals_by_category():
    lookup_category = input("Enter a category: ")

    # get return type
    categories = requests.get_categories()
    
    # handels exception if requests.get_categories() returns None
    if categories is not None:
        found = False
        # for loop that searches if lookup_category is in categories
        for i in range(len(categories)):
            category = categories[i]
            if category.get_category().lower() == lookup_category.lower():
                found = True
                break

        if found:
            meals = requests.get_meal_by_category(lookup_category)
            print()

            # if the category is found then all the meals for the
            # category that was searched gets printed
            if meals is not None:
                print("MEALS FOR " + lookup_category.upper())
                for i in range(len(meals)):
                    meal = meals[i]
                    print("  " + meal.get_meal_name())
                print()
            else:
                print("Technical difficulties, please try again later\n")
        else:
            print("invalid category. Please try again")
    else:
        print("\nTechnical difficulties, please try again later\n")



def list_areas():
    # get return type
    areas = requests.get_areas()

    # handels exception if requests.get_areas() returns None
    if areas is not None:
        print("AREAS")
        # for loop that assigns how over many indexes there are for the length of areas
        for i in range(len(areas)):
            area = areas[i]
            # prints each area by index
            print("  " + area.get_area())
        print()
    else:
        print("\nTechnical difficulties, please try again later\n")


def list_meals_by_area():
    lookup_area = input("Enter an area: ")

    # get return type
    areas = requests.get_areas()
    
    # handels exception if requests.get_areas() returns None
    if areas is not None:
        found = False
        # for loop that searches if lookup_area is in areas
        for i in range(len(areas)):
            area = areas[i]
            if area.get_area().lower() == lookup_area.lower():
                found = True
                break

        if found:
            meals = requests.get_meal_by_area(lookup_area)
            print()

            if meals is not None:
                # if the category is found then all the meals for the
                # category that was searched gets printed
                print("MEALS FOR " + lookup_area.upper())
                for i in range(len(meals)):
                    meal = meals[i]
                    print("  " + meal.get_meal_name())
                print()
            else:
                print("Technical difficulties, please try again later\n")
        else:
            print("invalid area. Please try again")
    else:
        print("\nTechnical difficulties, please try again later\n")


# function that takes the first letter of the meal name 
# and the index of the meal and returns the instructions
def instruction_index(first_letter, index):
    instructions = requests.get_meal_instructions(first_letter)

    if instructions is not None:
        meal_instructions = instructions[index]
        # text wrap will make the instructions have a limit 
        # of 80 characters per line
        wrapper = textwrap.TextWrapper(width=80)
        wrapped_instructions = wrapper.fill(text=meal_instructions.get_instructions())
    else:
        print("\nTechnical difficulties, please try again later\n")

    return wrapped_instructions


# function hat take the name of the meal and prints the 
# ingredients and measurements based on the meal
def list_ingredients(name):
    ingredients = requests.get_ingredients(name) 

    if ingredients is not None:
        for i in range(len(ingredients)):
            ingredient = ingredients[i]
            # formats measurements and ingredients into 2 neat collumns
            print("{:17} {:<10}".format(ingredient.get_measurement(), ingredient.get_ingredient()))
    else:
        print("\nTechnical difficulties, please try again later\n")


# promps user to seach for a meal to display its recipe with instructions and ingredients
def search_meals():
    name = input("SEARCH FOR MEAL: ")
    first_letter = name[0]
    meals = requests.get_all_meals(first_letter)

    if meals is not None:
        found = False 

        for i in range(len(meals)):
            meal = meals[i]
            if meal.get_meal_name().lower() == name.lower():
                found = True
                index = i
                break
        if found:
            print("\nRecipe: " + meal.get_meal_name())
            print("\nInstructions:\n" + instruction_index(first_letter, index))
            print("\nIngredients:")
            print("{:17} {:<10}".format("Measure", "Ingredient"))
            print("-"*80)
            list_ingredients(name)
        else:
            print("Invalid meal")

        print()
    else:
        print("\nTechnical difficulties, please try again later\n")


# Returns the name of a random meal
def get_random_meal_name():
    meal = requests.get_random_meal()

    if meal is not None:
        print("A random meal was selected just for you!")
        random_meal = meal[0]
    else:
        print("\nTechnical difficulties, please try again later\n")

    return random_meal.get_meal_name()


# takes the random meal name and displays its recipe with instructions and ingredients
def random_meal():
    random_meal = get_random_meal_name()
    first_letter = random_meal[0]
    meals = requests.get_all_meals(first_letter)

    if meals is not None:
        found = False 
        for i in range(len(meals)):
            meal = meals[i]
            if meal.get_meal_name().lower() == random_meal.lower():
                found = True
                index = i
                break
        if found:
            print("\nRecipe: " + random_meal )
            print("\nInstructions:\n" + instruction_index(first_letter, index))
            print("\nIngredients:")
            print("{:17} {:<10}".format("Measure", "Ingredient"))
            print("-"*80)
            list_ingredients(random_meal)
        else:
            print("No meal found")
    else:
        print("\nTechnical difficulties, please try again later\n")

def main():

    show_title()
    show_menu()

    # Loops the choices for the menu options
    while True:
        command = input("What would you like to do?: ")

        if command != "0" and command != "1" and command != "2" and command != "3" and command != "4" and command != "5" and command != "6" and command != "7":
            print("Please enter a valid choice on the menu 0-7\n")
            continue

        if command == "1":
            print()
            list_categories()
            print()
        elif command == "2":
            print()
            list_meals_by_category()
            print()
        elif command == "3":
            print()
            search_meals()
        elif command == "4":
            print()
            random_meal()
            print()
        elif command == "5":
            print()
            list_areas()
            print()
        elif command == "6":
            print()
            list_meals_by_area()
            print()
        elif command == "7":
            print()
            show_menu()
        elif command == "0":
            print("\nSee you soon!\n")
            break


if __name__ == "__main__":
    main()


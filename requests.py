# data layer

from urllib import request, parse
import json

from objects import Category, Meal, Area, Instructions, Ingredient


def get_categories():
    # api for all meal categories
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return categories


def get_meal_by_category(category):
    # api for all meals by category
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])

            meals.append(meal)
    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return meals


def get_areas():
    #api for all areas
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for area_data in data['meals']:
            area = Area(area_data['strArea'])

            areas.append(area)
    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return areas


def get_meal_by_area(area):
    # api for all meals by area
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])

            meals.append(meal)
    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return meals

def get_all_meals(first_letter):
    #api that has all meals by first letter
    url = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + first_letter 
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])

            meals.append(meal)

    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return meals


def get_meal_instructions(first_letter):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + first_letter 
    f = request.urlopen(url)
    instructions = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal_instructions = Instructions(meal_data['strInstructions'])

            instructions.append(meal_instructions)

    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return instructions


def get_ingredients(name):
    #api that gets meal attributes by the meal name
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + parse.quote(name)
    f = request.urlopen(url)
    ingredients = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
           for i in range(1,20):
               ingredient = Ingredient(meal_data['strIngredient' + str(i)], meal_data['strMeasure' + str(i)])
               if meal_data['strIngredient' + str(i)] != "" and meal_data['strMeasure' + str(i)] != "":
                   ingredients.append(ingredient)
    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return ingredients


def get_random_meal():
    #api that gets a random meal
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    f = request.urlopen(url)
    meal = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            rand_meal = Meal(meal_data['strMeal'])

            meal.append(rand_meal)

    except (ValueError, KeyError, TypeError):
        print("JSON format Error")
        return None

    return meal





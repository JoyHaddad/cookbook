# business layer

# class to get meal categories
class Category:
    def __init__(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

# class to get the name of a meal
class Meal:
    def __init__(self, meal_name):
        self.__meal_name = meal_name
    
    def get_meal_name(self):
        return self.__meal_name

# class to get areas for meals
class Area:
    def __init__(self, area):
        self.__area = area
    
    def get_area(self):
        return self.__area

# class to get meal instructions
class Instructions:
    def __init__(self, instructions):
        self.__instructions = instructions
    
    def get_instructions(self):
        return self.__instructions

# class to get meal ingredients and measurements
class Ingredient:
    def __init__(self, ingredient, measurement):
        self.__ingredient = ingredient
        self.__measurement = measurement

    def get_ingredient(self):
        return self.__ingredient

    def get_measurement(self):
        return self.__measurement
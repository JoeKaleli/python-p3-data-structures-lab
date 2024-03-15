spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []

    for food in spicy_foods:
        names.append(food['name'])

    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []

    for food in spicy_foods:

        if food['heat_level'] > 5:
            spiciest_foods.append(food)

        return spiciest_foods

def print_spicy_foods(spicy_foods):
    # Iterate over each dictionary in the list of spicy foods
    for food in spicy_foods:
        # Extract information about the spicy food
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        
        # Create a string of chili pepper emojis based on the heat level
        chili_peppers = '🌶' * heat_level
        
        # Print the spicy food in the specified format
        print(f"{name} ({cuisine}) | Heat Level: {chili_peppers}")
    
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
        
    return None


def get_spiciest_foods(spicy_foods):
    # Initialize an empty list to store the spiciest foods
    spiciest_foods = []
    
    # Iterate over each dictionary in the list of spicy foods
    for food in spicy_foods:
        # Check if the heat level of the current spicy food is greater than 5
        if food['heat_level'] > 5:
            # If the heat level is greater than 5, append the food dictionary to the spiciest_foods list
            spiciest_foods.append(food)
    
    # Return the list of spiciest foods
    return spiciest_foods

def print_spiciest_foods(spicy_foods):
    # Get the list of spiciest foods using the get_spiciest_foods() function
    spiciest = get_spiciest_foods(spicy_foods)
    
    # Print the spiciest foods using the print_spicy_foods() function
    print_spicy_foods(spiciest)


    

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_spicy_foods = len(spicy_foods)

    for food in spicy_foods:
        total_heat_level += food['heat_level']

    if num_spicy_foods != 0:
        average = total_heat_level / num_spicy_foods
    else :
        average = 0

    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    return spicy_foods

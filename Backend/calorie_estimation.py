# Example of food items and their calorie values per 100g
food_calories = {
    'apple': 52,
    'banana': 96,
    'orange': 43,
    'chicken': 165,
    'rice': 130,
    # Add more food items here
}

def estimate_calories(food_item):
    # Look up calories for the food item
    calories_per_100g = food_calories.get(food_item.lower(), 0)

    # If the food item is found, estimate the total calories based on a portion size
    # Let's assume a portion size of 200g for simplicity
    total_calories = calories_per_100g * 2  # 200g portion

    return calories_per_100g, total_calories

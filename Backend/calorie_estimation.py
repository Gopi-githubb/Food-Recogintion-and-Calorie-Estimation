import logging

# Dictionary of food items and their calorie values per 100g
food_calories = {
    'apple': 52,
    'banana': 96,
    'orange': 43,
    'chicken': 165,
    'rice': 130,
    'egg': 143,
    'carrot': 41,
    'broccoli': 55,
    # Add more food items here as needed
}

def estimate_calories(food_item, portion_size=200):
    """
    Estimates the calories for a given food item based on its portion size.

    Parameters:
    - food_item (str): The name of the food item.
    - portion_size (float): The portion size in grams. Default is 200g.

    Returns:
    - dict: A dictionary containing calories per 100g and total calories for the portion size.
    """
    try:
        # Validate the portion size
        if not isinstance(portion_size, (int, float)) or portion_size <= 0:
            error_message = "Invalid portion size. Please provide a positive number."
            logging.error(error_message)
            return {"message": error_message, "calories": 0}

        # Validate the food_item is a string
        if not isinstance(food_item, str) or not food_item.strip():
            error_message = "Food item must be a non-empty string."
            logging.error(error_message)
            return {"message": error_message, "calories": 0}

        # Convert the food item to lowercase for case-insensitive matching
        food_item = food_item.strip().lower()

        # Look up calories for the food item
        calories_per_100g = food_calories.get(food_item)

        if calories_per_100g is None:
            # If food item is not found, return a message indicating it
            error_message = f"Food item '{food_item}' not found in the database. Please check the name or add it to the database."
            logging.warning(error_message)
            return {"message": error_message, "calories": 0}

        # Estimate total calories based on portion size
        total_calories = (calories_per_100g * portion_size) / 100  # Portion size in grams

        # Format the result for better readability (two decimal places)
        total_calories = round(total_calories, 2)

        # Log the successful lookup and estimation
        logging.info(f"Food item: {food_item}, Calories per 100g: {calories_per_100g}, Portion size: {portion_size}g, Total calories: {total_calories}")

        return {"food_item": food_item, "calories_per_100g": calories_per_100g, "total_calories": total_calories}

    except Exception as e:
        # General exception handling if something goes wrong
        logging.error(f"An error occurred: {str(e)}")
        return {"message": f"An error occurred: {str(e)}", "calories": 0}


# Function to add new food items
def add_food_item(food_item, calories_per_100g):
    """
    Adds a new food item to the food_calories dictionary.

    Parameters:
    - food_item (str): The name of the food item.
    - calories_per_100g (float): The calorie value per 100 grams of the food item.

    Returns:
    - bool: True if the item was added successfully, False if it already exists.
    """
    if food_item.strip().lower() in food_calories:
        logging.warning(f"Food item '{food_item}' already exists.")
        return False
    food_calories[food_item.strip().lower()] = calories_per_100g
    logging.info(f"Added {food_item} with {calories_per_100g} calories per 100g.")
    return True

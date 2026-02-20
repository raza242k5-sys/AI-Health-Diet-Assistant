def diet_recommendation(calories, goal):
    
    if goal == "Weight Loss":
        calories -= 500
    elif goal == "Weight Gain":
        calories += 500
    
    meal_plan = {
        "Breakfast": "Oats + Banana + Boiled Eggs",
        "Lunch": "Brown Rice + Dal + Salad",
        "Dinner": "Grilled Paneer/Chicken + Veggies",
        "Snacks": "Almonds + Fruits"
    }

    return calories, meal_plan

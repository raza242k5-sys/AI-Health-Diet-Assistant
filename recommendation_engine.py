import random

def diet_recommendation(calories, goal, diet_type, gym, disease):

    # =============================
    # Adjust Calories Based on Goal
    # =============================
    if goal == "Weight Loss":
        calories -= 300
    elif goal == "Weight Gain":
        calories += 300

    # =============================
    # Gym Effect (Higher protein)
    # =============================
    if gym == "Yes":
        calories += 200

    # =============================
    # Meal Distribution
    # =============================
    breakfast_cal = round(calories * 0.25)
    lunch_cal = round(calories * 0.35)
    dinner_cal = round(calories * 0.30)
    snacks_cal = round(calories * 0.10)

    # =============================
    # Food Options (Veg / Non-Veg)
    # =============================

    veg_breakfast = [
        "Oats + Milk + Banana",
        "Poha + Peanuts",
        "Upma + Fruit",
        "Paratha + Curd"
    ]

    nonveg_breakfast = [
        "Oats + Eggs",
        "Boiled Eggs + Toast",
        "Omelette + Bread",
        "Egg Sandwich"
    ]

    veg_lunch = [
        "Rice + Dal + Salad",
        "Chapati + Paneer + Veggies",
        "Rajma + Rice",
        "Khichdi + Curd"
    ]

    nonveg_lunch = [
        "Chicken + Rice + Salad",
        "Egg Curry + Chapati",
        "Fish + Rice",
        "Chicken + Chapati"
    ]

    veg_dinner = [
        "Paneer + Chapati",
        "Dal + Rice",
        "Vegetable Soup + Bread",
        "Mixed Veg + Chapati"
    ]

    nonveg_dinner = [
        "Grilled Chicken + Veggies",
        "Egg Curry + Chapati",
        "Fish + Salad",
        "Chicken Soup"
    ]

    snacks_common = [
        "Nuts + Fruits",
        "Protein Shake",
        "Peanut Butter Sandwich",
        "Fruit Salad"
    ]

    # =============================
    # Select Diet Type
    # =============================

    if diet_type == "Vegetarian":
        breakfast = random.choice(veg_breakfast)
        lunch = random.choice(veg_lunch)
        dinner = random.choice(veg_dinner)
    else:
        breakfast = random.choice(nonveg_breakfast)
        lunch = random.choice(nonveg_lunch)
        dinner = random.choice(nonveg_dinner)

    snacks = random.choice(snacks_common)

    # =============================
    # Gym → High Protein Add
    # =============================
    if gym == "Yes":
        breakfast += " + Protein Source"
        lunch += " + High Protein"
        dinner += " + Protein Rich"

    # =============================
    # Disease Conditions
    # =============================
    if disease == "Diabetes":
        breakfast += " (Low Sugar)"
        lunch += " (Low GI)"
        dinner += " (Low Carb)"

    elif disease == "Heart Disease":
        breakfast += " (Low Fat)"
        lunch += " (Low Cholesterol)"
        dinner += " (Healthy Fats)"

    # =============================
    # Final Meal Plan
    # =============================

    meal_plan = {
        "Breakfast": f"{breakfast_cal} kcal → {breakfast}",
        "Lunch": f"{lunch_cal} kcal → {lunch}",
        "Dinner": f"{dinner_cal} kcal → {dinner}",
        "Snacks": f"{snacks_cal} kcal → {snacks}"
    }

    return calories, meal_plan
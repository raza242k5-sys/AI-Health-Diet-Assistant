def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr, 2)

def daily_calories(bmr, activity_level):
    activity_multiplier = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725
    }
    return round(bmr * activity_multiplier[activity_level], 2)

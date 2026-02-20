import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("diet_dataset.csv")

# Encode categorical data
le_gender = LabelEncoder()
le_activity = LabelEncoder()
le_goal = LabelEncoder()

data["gender"] = le_gender.fit_transform(data["gender"])
data["activity_level"] = le_activity.fit_transform(data["activity_level"])
data["goal"] = le_goal.fit_transform(data["goal"])

X = data[["age", "gender", "height", "weight", "activity_level", "goal"]]
y = data["calories"]

model = RandomForestRegressor()
model.fit(X, y)

def predict_calories(age, gender, height, weight, activity, goal):
    gender = le_gender.transform([gender])[0]
    activity = le_activity.transform([activity])[0]
    goal = le_goal.transform([goal])[0]
    
    prediction = model.predict([[age, gender, height, weight, activity, goal]])
    return round(prediction[0], 2)

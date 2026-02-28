import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# ==============================
# Load Dataset
# ==============================

try:
    data = pd.read_csv("diet_dataset.csv")
except FileNotFoundError:
    raise Exception("⚠ diet_dataset.csv not found in project folder.")


# ==============================
# Encode Categorical Features
# ==============================

le_gender = LabelEncoder()
le_activity = LabelEncoder()
le_goal = LabelEncoder()

data["gender"] = le_gender.fit_transform(data["gender"])
data["activity_level"] = le_activity.fit_transform(data["activity_level"])
data["goal"] = le_goal.fit_transform(data["goal"])


# ==============================
# Feature Selection
# ==============================

feature_columns = ["age", "gender", "height", "weight", "activity_level", "goal"]

X = data[feature_columns]
y = data["calories"]


# ==============================
# Model Training (Full Dataset)
# ==============================

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)


# ==============================
# Prediction Function
# ==============================

def predict_calories(age, gender, height, weight, activity, goal):
    try:
        # Encode categorical inputs
        gender_encoded = le_gender.transform([gender])[0]
        activity_encoded = le_activity.transform([activity])[0]
        goal_encoded = le_goal.transform([goal])[0]

        # Create DataFrame (prevents sklearn warning)
        input_df = pd.DataFrame([{
            "age": age,
            "gender": gender_encoded,
            "height": height,
            "weight": weight,
            "activity_level": activity_encoded,
            "goal": goal_encoded
        }])

        prediction = model.predict(input_df)

        return round(prediction[0], 2)

    except Exception as e:
        return f"⚠ Prediction Error: {str(e)}"
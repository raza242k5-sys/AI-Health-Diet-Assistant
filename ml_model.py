import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

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
# Train / Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==============================
# Model Training
# ==============================

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# ==============================
# Model Evaluation
# ==============================

predictions = model.predict(X_test)
r2 = r2_score(y_test, predictions)

print(f"Model R² Score: {round(r2, 3)}")


# ==============================
# Prediction Function
# ==============================

def predict_calories(age, gender, height, weight, activity, goal):
    try:
        # Encode inputs
        gender_encoded = le_gender.transform([gender])[0]
        activity_encoded = le_activity.transform([activity])[0]
        goal_encoded = le_goal.transform([goal])[0]

        # Create DataFrame (fixes sklearn feature name warning)
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
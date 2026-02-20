import streamlit as st
import random

from health_calculator import calculate_bmi, bmi_category, calculate_bmr, daily_calories
from recommendation_engine import diet_recommendation
from ml_model import predict_calories
from chatbot import ask_health_question

st.set_page_config(page_title="AI Health Assistant", page_icon="🧠", layout="wide")


st.title(" AI Health & Diet Recommendation System")

st.sidebar.header("Enter Your Details")

age = st.sidebar.number_input("Age", 10, 100)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", 100, 220)
weight = st.sidebar.number_input("Weight (kg)", 30, 200)
activity = st.sidebar.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])
goal = st.sidebar.selectbox("Goal", ["Weight Loss", "Weight Gain", "Maintain Weight"])

if st.sidebar.button("Generate Plan"):
    
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    predicted_calories = predict_calories(age, gender, height, weight, activity, goal)
    final_calories, meal_plan = diet_recommendation(predicted_calories, goal)


    st.subheader(" Health Analysis")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Category:** {category}")
    st.write(f"**Daily Calorie Need:** {final_calories} kcal")

    st.subheader(" Recommended Meal Plan")
    for meal, food in meal_plan.items():
        st.write(f"**{meal}:** {food}")

    st.subheader(" Weekly Weight Progress (Sample Data)")
    
    sample_weights = []
    current_weight = weight

    for i in range(7):
        current_weight -= random.uniform(0, 0.5)
        sample_weights.append(round(current_weight, 2))

    st.line_chart(sample_weights)

    # -----------------------------
# 🤖 AI CHATBOT SECTION
# -----------------------------

st.subheader("🤖 AI Health Assistant")

user_question = st.text_input("Ask a health-related question:")

if st.button("Ask AI"):
    if user_question.strip() != "":
        answer = ask_health_question(user_question)
        st.write("### 🤖 AI Response:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")




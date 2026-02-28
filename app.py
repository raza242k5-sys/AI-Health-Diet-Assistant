import streamlit as st
import random

from health_calculator import calculate_bmi, bmi_category
from recommendation_engine import diet_recommendation
from ml_model import predict_calories
from chatbot import ask_health_question

# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Health & Diet Recommendation System")

# ==============================
# Sidebar Inputs
# ==============================

st.sidebar.header("Enter Your Details")

age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=220, value=170)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
activity = st.sidebar.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])
goal = st.sidebar.selectbox("Goal", ["Weight Loss", "Weight Gain", "Maintain Weight"])

# ==============================
# Generate Plan Button
# ==============================

if st.sidebar.button("Generate Plan"):

    # Input validation
    if weight <= 0 or height <= 0:
        st.error("⚠ Height and Weight must be greater than 0.")
    else:
        try:
            with st.spinner("Generating your personalized health plan..."):

                # BMI Calculation
                bmi = calculate_bmi(weight, height)
                category = bmi_category(bmi)

                # ML Prediction
                predicted_calories = predict_calories(
                    age, gender, height, weight, activity, goal
                )

                # Diet Recommendation
                final_calories, meal_plan = diet_recommendation(
                    predicted_calories, goal
                )

            # ==============================
            # Display Results
            # ==============================

            st.subheader("📊 Health Analysis")
            st.write(f"**BMI:** {bmi}")
            st.write(f"**Category:** {category}")
            st.write(f"**Daily Calorie Need:** {final_calories} kcal")

            st.subheader("🍽 Recommended Meal Plan")
            for meal, food in meal_plan.items():
                st.write(f"**{meal}:** {food}")

            # Weekly Weight Progress Chart
            st.subheader("📈 Weekly Weight Progress (Sample Data)")

            sample_weights = []
            current_weight = weight

            for _ in range(7):
                if goal == "Weight Loss":
                    current_weight -= random.uniform(0, 0.5)
                elif goal == "Weight Gain":
                    current_weight += random.uniform(0, 0.5)
                sample_weights.append(round(current_weight, 2))

            st.line_chart(sample_weights)

        except Exception as e:
            st.error(f"⚠ Something went wrong: {str(e)}")

# ==============================
# AI Chatbot Section
# ==============================

st.subheader("🤖 AI Health Assistant")

user_question = st.text_input("Ask a health-related question:")

if st.button("Ask AI"):

    if user_question.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Thinking..."):
            answer = ask_health_question(user_question)

        st.write("### 🤖 AI Response:")
        st.write(answer)
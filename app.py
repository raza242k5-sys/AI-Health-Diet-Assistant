import streamlit as st

from health_calculator import calculate_bmi, bmi_category
from recommendation_engine import diet_recommendation
from ml_model import predict_calories
from chatbot import ask_health_question

# =============================
# Page Config
# =============================
st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🩺",
    layout="wide"
)

# =============================
# Custom Styling
# =============================
st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: bold;
    color: #2E86C1;
}
.section {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# Title
# =============================
st.markdown('<div class="main-title">🩺 AI Health & Diet Assistant</div>', unsafe_allow_html=True)

# =============================
# Sidebar Inputs
# =============================
st.sidebar.header("🧾 Patient Details")

age = st.sidebar.number_input("Age", 10, 100)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", 100, 220)
weight = st.sidebar.number_input("Weight (kg)", 30, 200)

activity = st.sidebar.selectbox(
    "Activity Level",
    ["Sedentary", "Light", "Moderate", "Active"]
)

goal = st.sidebar.selectbox(
    "Goal",
    ["Weight Loss", "Weight Gain", "Maintain Weight"]
)

diet_type = st.sidebar.selectbox(
    "Diet Type",
    ["Vegetarian", "Non-Vegetarian"]
)

gym = st.sidebar.selectbox("Workout", ["No", "Yes"])

disease = st.sidebar.selectbox(
    "Health Condition",
    ["None", "Diabetes", "Heart Disease"]
)

# =============================
# Always Calculate Data
# =============================
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

predicted_calories = predict_calories(
    age, gender, height, weight, activity, goal
)

final_calories, meal_plan = diet_recommendation(
    predicted_calories, goal, diet_type, gym, disease
)

# =============================
# Generate Plan Button
# =============================
if st.sidebar.button("🧠 Generate Health Plan"):

    try:
        # Health Analysis
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📊 Health Analysis")

        col1, col2, col3 = st.columns(3)
        col1.metric("BMI", bmi)
        col2.metric("Category", category)
        col3.metric("Calories", f"{final_calories} kcal")

        st.markdown('</div>', unsafe_allow_html=True)

        # Diet Plan
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("🍽 Recommended Diet Plan")

        for meal, food in meal_plan.items():
            st.write(f"**{meal}:** {food}")

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error generating plan: {e}")

# =============================
# 🤖 PERSONAL AI DOCTOR CHATBOT
# =============================
st.markdown('<div class="section">', unsafe_allow_html=True)

st.subheader("🤖 AI Health Assistant")

user_question = st.text_input("Ask a medical or health question")

if st.button("Ask AI"):

    if user_question.strip() == "":
        st.warning("Please enter a question")

    else:
        try:
            user_data = {
                "age": age,
                "gender": gender,
                "bmi": bmi,
                "category": category,
                "calories": final_calories,
                "goal": goal,
                "diet_type": diet_type,
                "gym": gym,
                "disease": disease
            }

            with st.spinner("Consulting AI doctor..."):
                answer = ask_health_question(user_question, user_data)

            st.success(answer)

        except Exception as e:
            st.error(f"API Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
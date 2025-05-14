import streamlit as st

# Set page title and header with emojis
st.title("BMI Calculator 🩺💪")
st.header("Calculate Your Body Mass Index 📏")

# Instructions with emojis
st.write("Enter your weight in kilograms and height in meters to calculate your BMI! 🏋️‍♂️")

# Input fields with emoji labels
weight = st.number_input("Weight (kg) ⚖️", min_value=0.0, value=70.0, step=0.1)
height = st.number_input("Height (m) 📐", min_value=0.0, value=1.75, step=0.01)

# Calculate BMI when button is clicked
if st.button("Calculate BMI 🚀"):
    if height > 0:  # Prevent division by zero
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        # Determine BMI category with emoji indicators
        if bmi < 18.5:
            category = "Underweight 😔"
        elif 18.5 <= bmi < 25:
            category = "Normal ✅"
        elif 25 <= bmi < 30:
            category = "Overweight ⚠️"
        else:
            category = "Obese ❗"
        
        # Display results with emojis
        st.success(f"Your BMI is: **{bmi}** 🎯")
        st.info(f"Category: **{category}** 🔔")
    else:
        st.error("Height must be greater than 0. 🚫")

# Add a note about BMI ranges with emojis
st.markdown("""
### BMI Categories 🌟:
- **Underweight** 😔: < 18.5
- **Normal** ✅: 18.5 - 24.9
- **Overweight** ⚠️: 25 - 29.9
- **Obese** ❗: ≥ 30
""")
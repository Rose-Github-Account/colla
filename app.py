
import streamlit as st

st.title("BMI Calculator 🧑‍⚕️")
st.write("Enter your height and weight to calculate your BMI. 📊")

# Input for height and weight
height = st.number_input("Height (in meters) 🏋️‍♂️", min_value=0.5, max_value=3.0, value=1.75, step=0.01)
weight = st.number_input("Weight (in kilograms) ⚖️", min_value=10, max_value=90, value=70, step=1)

# Button to calculate BMI
if st.button("Calculate BMI 🧮"):
    if height > 0 and weight > 0:
        # Calculate BMI
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # Display BMI category based on the calculated value
        if bmi < 18.5:
            st.warning("You are underweight 🏃‍♀️")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight 🙂")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight 😕")
        else:
            st.error("You are obese 🛑")

    else:
        st.error("Please enter valid height and weight values! ⚠️")

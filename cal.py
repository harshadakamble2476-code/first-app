import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.write("Enter two numbers and select an operation.")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Choose Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate result
result = None

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")

    if result is not None:
        st.success(f"Result: {result}")

# Tip
st.caption(
    "Tip: You can modify this calculator by adding scientific functions like square root, power, or percentage."
)

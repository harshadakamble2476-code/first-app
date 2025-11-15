import streamlit as st
from math import sqrt

st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("A tiny calculator built with Streamlit. Supports basic arithmetic and a few functions.")

# Input area
col1, col2 = st.columns([2,1])
with col1:
    expr = st.text_input("Enter an expression (example: 12 + 3*4 or sqrt(16) + 5):", value="12+3*4")
with col2:
    if st.button("Calculate"):
        pass

# Prebuilt buttons
st.markdown("**Quick operations:**")
c1, c2, c3, c4 = st.columns(4)
if c1.button("7"): expr = expr + "7"
if c2.button("8"): expr = expr + "8"
if c3.button("9"): expr = expr + "9"
if c4.button("/"): expr = expr + "/"

c5, c6, c7, c8 = st.columns(4)
if c5.button("4"): expr = expr + "4"
if c6.button("5"): expr = expr + "5"
if c7.button("6"): expr = expr + "6"
if c8.button("*"): expr = expr + "*"

c9, c10, c11, c12 = st.columns(4)
if c9.button("1"): expr = expr + "1"
if c10.button("2"): expr = expr + "2"
if c11.button("3"): expr = expr + "3"
if c12.button("-"): expr = expr + "-"

c13, c14, c15, c16 = st.columns(4)
if c13.button("0"): expr = expr + "0"
if c14.button("."): expr = expr + "."
if c15.button("+"): expr = expr + "+"
if c16.button("C"): expr = ""

# Extra functions
st.markdown("**Functions:** (use in expression: e.g. sqrt(25) )")
st.write("Available: `sqrt()`")

# Evaluate safely
result = None
error = None
if expr.strip() != "":
    try:
        # Safe eval: only expose very limited names
        allowed_names = {"sqrt": sqrt}
        # eval expression using only math functions above and no builtins
        result = eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        error = str(e)

st.write("**Expression:**", f"`{expr}`")
if error:
    st.error(f"Error: {error}")
else:
    st.success(f"Result: {result}")

# Optional: small history stored in session state
if "history" not in st.session_state:
    st.session_state.history = []
if st.button("Save to history") and not error:
    st.session_state.history.append((expr, result))

if st.session_state.history:
    st.markdown("**History**")
    for i, (e, r) in enumerate(reversed(st.session_state.history[-10:]), 1):
        st.write(f"{i}. `{e}` = **{r}**")

st.caption("Tip: You can use

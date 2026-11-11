
# app_sigmoid.py
# Streamlit app: Sigmoid Activation Function Visualizer

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Sigmoid Activation Function",
    layout="wide"
)

# Application title
st.title("Sigmoid Activation Function")
st.write("Visualise the Sigmoid activation function and its output.")

# --- Activation function ---
st.subheader("Sigmoid Activation Function")

st.latex(r"f(x) = \frac{1}{1+e^{-x}}")

def act_curve(name, x):
    if name == "sigmoid":
        return 1 / (1 + np.exp(-x))

# --- User input ---
st.subheader("Input Value")

x_value = st.slider(
    "Select input value (x)",
    min_value=-6.0,
    max_value=6.0,
    value=2.0,
    step=0.1
)

# Calculate output
y_value = act_curve("sigmoid", x_value)

st.write(f"**Input (x):** {x_value:.2f}")
st.write(f"**Output f(x):** {y_value:.4f}")

# --- Plot activation function ---
xgrid = np.linspace(-6, 6, 400)

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(
    xgrid,
    act_curve("sigmoid", xgrid),
    label="Sigmoid",
    linewidth=2
)

ax.scatter(
    x_value,
    y_value,
    color="red",
    s=80,
    label="Selected Input"
)

ax.legend()
ax.grid(True)
ax.set_title("Sigmoid Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.set_ylim(-0.1, 1.1)

st.pyplot(fig)
plt.close(fig)

# --- Interpretation ---
st.subheader("Interpretation")

st.write(
    "Sigmoid transforms input values into output values "
    "between 0 and 1, producing an S-shaped curve."
)
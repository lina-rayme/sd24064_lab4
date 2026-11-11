
# app_relu.py
# Streamlit app: ReLU Activation Function Visualizer

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="ReLU Activation Function",
    layout="wide"
)

# Application title
st.title("Rectified Linear Unit (ReLU)")
st.write("Visualise the ReLU activation function and its output.")

# --- Activation function ---
st.subheader("ReLU Activation Function")

st.latex(r"f(x) = \max(0,x)")

def act_curve(name, x):
    if name == "relu":
        return np.maximum(0, x)

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
y_value = act_curve("relu", x_value)

st.write(f"**Input (x):** {x_value:.2f}")
st.write(f"**Output f(x):** {y_value:.4f}")

# --- Plot activation function ---
xgrid = np.linspace(-6, 6, 400)

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(
    xgrid,
    act_curve("relu", xgrid),
    label="ReLU",
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
ax.set_title("ReLU Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")

st.pyplot(fig)
plt.close(fig)

# --- Interpretation ---
st.subheader("Interpretation")

st.write(
    "ReLU returns 0 when the input is negative "
    "and returns the input value when the input is positive."
)
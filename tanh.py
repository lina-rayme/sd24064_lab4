
# app_tanh.py
# Streamlit app: Tanh Activation Function Visualizer

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Tanh Activation Function",
    layout="wide"
)

# Application title
st.title("Hyperbolic Tangent (Tanh)")
st.write("Visualise the Tanh activation function and its output.")

# --- Activation function ---
st.subheader("Tanh Activation Function")

st.latex(r"f(x) = \tanh(x)")

def act_curve(name, x):
    if name == "tanh":
        return np.tanh(x)

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
y_value = act_curve("tanh", x_value)

st.write(f"**Input (x):** {x_value:.2f}")
st.write(f"**Output f(x):** {y_value:.4f}")

# --- Plot activation function ---
xgrid = np.linspace(-6, 6, 400)

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(
    xgrid,
    act_curve("tanh", xgrid),
    label="Tanh",
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
ax.set_title("Tanh Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.set_ylim(-1.2, 1.2)

st.pyplot(fig)
plt.close(fig)

# --- Interpretation ---
st.subheader("Interpretation")

st.write(
    "Tanh transforms input values into output values "
    "between -1 and 1, producing an S-shaped curve."
)
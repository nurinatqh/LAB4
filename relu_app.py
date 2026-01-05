import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation Function", layout="centered")

st.title("ReLU Activation Function")
st.write("Rectified Linear Unit (ReLU): f(x) = max(0, x)")

x_min, x_max = st.sidebar.slider("X range", -10, 0, -5), st.sidebar.slider("X range ", 0, 10, 5)

x = np.linspace(x_min, x_max, 400)
y = np.maximum(0, x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("ReLU(x)")
ax.set_title("ReLU Activation Function")
ax.grid(True)

st.pyplot(fig)

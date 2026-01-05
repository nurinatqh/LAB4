import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation Function", layout="centered")

st.title("Sigmoid Activation Function")
st.write("Sigmoid: f(x) = 1 / (1 + e^(-x))")

x = np.linspace(-10, 10, 400)
y = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("Sigmoid(x)")
ax.set_title("Sigmoid Activation Function")
ax.grid(True)

st.pyplot(fig)

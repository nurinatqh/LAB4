import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation Function", layout="centered")

st.title("Tanh Activation Function")
st.write("Hyperbolic Tangent: f(x) = tanh(x)")

x = np.linspace(-10, 10, 400)
y = np.tanh(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("tanh(x)")
ax.set_title("Tanh Activation Function")
ax.grid(True)

st.pyplot(fig)

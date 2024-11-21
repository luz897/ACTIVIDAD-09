import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Optimización No Lineal")
st.write("Este programa analiza la convexidad y concavidad de diversas funciones matemáticas.")

# Ejercicio 1
st.header("Ejercicio 1: \( f(x) = 3x + 2 \)")
st.write("Convexidad de la función \( f(x) = 3x + 2 \).")

def f1(x):
    return 3 * x + 2

x_points = [-2, -1, 0, 1, 2]
y_points = [f1(x) for x in x_points]
x = np.linspace(-3, 3, 100)
y = f1(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = 3x + 2", color="blue")
ax.scatter(x_points, y_points, color="red", label="Puntos evaluados")
ax.set_title("Gráfica de \( f(x) = 3x + 2 \)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid()
ax.legend()
st.pyplot(fig)
st.write("La función es convexa porque su segunda derivada es \( f''(x) = 0 \) y no cambia de curvatura.")

# Ejercicio 2
st.header("Ejercicio 2: \( f(x) = x^3 \)")
st.write("Analizar la convexidad o concavidad de la función.")

def f2(x):
    return x**3

x_points = [-2, -1, 0, 1, 2]
y_points = [f2(x) for x in x_points]
x = np.linspace(-2.5, 2.5, 100)
y = f2(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = x^3", color="green")
ax.scatter(x_points, y_points, color="red", label="Puntos evaluados")
ax.set_title("Gráfica de \( f(x) = x^3 \)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid()
ax.legend()
st.pyplot(fig)
st.write("La función es convexa para \( x > 0 \) y cóncava para \( x < 0 \).")

# Ejercicio 3
st.header("Ejercicio 3: \( f(x) = e^{2x} \)")
st.write("Analizar la convexidad de la función.")

def f3(x):
    return np.exp(2 * x)

x_points = [-1, -0.5, 0, 0.5, 1]
y_points = [f3(x) for x in x_points]
x = np.linspace(-1.5, 1.5, 100)
y = f3(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = e^{2x}", color="red")
ax.scatter(x_points, y_points, color="blue", label="Puntos evaluados")
ax.set_title("Gráfica de \( f(x) = e^{2x} \)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid()
ax.legend()
st.pyplot(fig)
st.write("La función es convexa porque \( f''(x) = 4e^{2x} > 0 \) para todo \( x \).")

# Ejercicio 4
st.header("Ejercicio 4: \( f(x) = \ln(x) \)")
st.write("Analizar la convexidad o concavidad de la función.")

def f4(x):
    return np.log(x)

x_points = [0.5, 1, 2, 3, 4]
y_points = [f4(x) for x in x_points]
x = np.linspace(0.1, 5, 100)
y = f4(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = ln(x)", color="purple")
ax.scatter(x_points, y_points, color="orange", label="Puntos evaluados")
ax.set_title("Gráfica de \( f(x) = \ln(x) \)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid()
ax.legend()
st.pyplot(fig)
st.write("La función es cóncava porque \( f''(x) = -1/x^2 < 0 \) para todo \( x > 0 \).")

# Ejercicio 5
st.header("Ejercicio 5: \( f(x) = x^4 - 2x^2 + 1 \)")
st.write("Analizar intervalos de convexidad, concavidad y puntos de inflexión.")

def f5(x):
    return x**4 - 2*x**2 + 1

def f5_second_derivative(x):
    return 12 * x**2 - 4

x_points = [-2, -1, 0, 1, 2]
y_points = [f5(x) for x in x_points]
x = np.linspace(-2.5, 2.5, 500)
y = f5(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = \(x^4 - 2x^2 + 1\)", color="blue")
ax.scatter(x_points, y_points, color="red", label="Puntos evaluados")
ax.axhline(0, color="gray", linestyle="--", linewidth=0.5, label="Eje x")
ax.set_title("Gráfica de \( f(x) = x^4 - 2x^2 + 1 \)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid()
ax.legend()
st.pyplot(fig)

critical_points = np.sqrt(1/3) * np.array([-1, 1])
st.write("### Intervalos de Convexidad y Concavidad:")
intervals = [(-np.inf, critical_points[0]), 
             (critical_points[0], critical_points[1]), 
             (critical_points[1], np.inf)]

for interval in intervals:
    midpoint = (interval[0] + interval[1]) / 2 if np.isfinite(interval[1]) else interval[0] + 1
    concavity = f5_second_derivative(midpoint)
    if concavity > 0:
        st.write(f"Convexo en el intervalo: {interval}")
    elif concavity < 0:
        st.write(f"Cóncavo en el intervalo: {interval}")

st.write("### Puntos de Inflexión:")
inflection_points = []
for cp in critical_points:
    left_sign = f5_second_derivative(cp - 0.01)
    right_sign = f5_second_derivative(cp + 0.01)
    if np.sign(left_sign) != np.sign(right_sign):
        inflection_points.append(cp)

if inflection_points:
    for ip in inflection_points:
        st.write(f"Punto de inflexión en \( x = {ip:.4f} \)")
else:
    st.write("No hay puntos de inflexión en el dominio considerado.")

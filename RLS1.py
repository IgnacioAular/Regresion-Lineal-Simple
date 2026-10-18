
import matplotlib.pyplot as plt

# Datos
x = [10, 15, 20, 25, 30, 35]  # Edad de los pacientes
y = [2.6, 3.1, 4.0, 4.3, 5.4, 6.1]  # Dias de observacion hospitalaria

n = len(x)

# Calcular las sumas
suma_x = sum(x)
suma_y = sum(y)
suma_xy = sum(xi * yi for xi, yi in zip(x, y))
suma_x2 = sum(xi**2 for xi in x)

# Calcular la pendiente y la interseccion
m = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x**2)
b = (suma_y / n) - m * (suma_x / n)

print("Resultado de la regresion lineal:")
print(f"Pendiente (m): {m:.4f}")
print(f"Interseccion (b): {b:.4f}")
print(f"Ecuacion: Dias = {m:.4f} * Edad + {b:.4f}")

# Calcular los valores predichos
y_pred = [m * xi + b for xi in x]

# Crear la grafica
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="darkblue", s=60, label="Datos reales")
plt.plot(
    x,
    y_pred,
    color="crimson",
    linewidth=2,
    label=f"Recta: y = {m:.4f} * x + {b:.4f}"
)

plt.xlabel("Edad del paciente (anos)", fontsize=11)
plt.ylabel("Dias de observacion hospitalaria", fontsize=11)
plt.title("Edad del paciente vs. dias de observacion hospitalaria",
          fontsize=13, pad=15)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

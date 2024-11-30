import numpy as np
import matplotlib.pyplot as plt

a, b, m, n = 0.5, 0.4, 0.3, 0.2
r, s = 0.1, -0.1
def richardson_model(t, vars):
    x, y = vars
    dx_dt = a * y - m * x + r
    dy_dt = b * x - n * y + s
    return [dx_dt, dy_dt]
x_vals = np.linspace(-1, 1, 20)
y_vals = np.linspace(-1, 1, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U = a * Y - m * X + r  # dx/dt
V = b * X - n * Y + s  # dy/dt
magnitude = np.sqrt(U**2 + V**2)
U_norm = U / magnitude
V_norm = V / magnitude

plt.figure(figsize=(10, 6))
plt.quiver(X, Y, U_norm, V_norm, color="blue", alpha=0.7)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Phase Plane of the Richardson Arms Race Model")
plt.xlabel("x (Expenditure of Country 1)")
plt.ylabel("y (Expenditure of Country 2)")
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

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
U = a * Y - m * X + r
V = b * X - n * Y + s
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

a, b, c, e, f = 0.5, 0.02, 0.01, 0.1, 0.1
def predator_prey(t, z):
    x, y = z
    dx_dt = a * x - b * x**2 - c * x * y
    dy_dt = e * x * y - f * y
    return [dx_dt, dy_dt]

initial_conditions = [
    [0.5, 20],
    [2, 60],
    [1.5, 30]
]

t_span = (0, 50)
t_eval = np.linspace(0, 50, 500)

trajectories = []
for ic in initial_conditions:
    solution = solve_ivp(predator_prey, t_span, ic, t_eval=t_eval)
    trajectories.append(solution.y)

plt.figure(figsize=(10, 6))

for trajectory, ic in zip(trajectories, initial_conditions):
    x, y = trajectory
    plt.plot(x, y, label=f"IC: x(0)={ic[0]}, y(0)={ic[1]}")

x = np.linspace(0, 3, 200)
y_nullcline = (a - b * x) / c
x_nullcline = [f / e] * len(x)

plt.plot(x, y_nullcline, 'r--', label="dx/dt = 0 (Prey Nullcline)")
plt.axvline(f / e, color='g', linestyle='--', label="dy/dt = 0 (Predator Nullcline)")
fixed_x = f / e
fixed_y = (a * e - b * f) / (c * e)
plt.scatter(fixed_x, fixed_y, color='black', label=f"Fixed Point: ({fixed_x:.2f}, {fixed_y:.2f})")
plt.title("Phase Plane of Predator-Prey System with Logistic Prey Model")
plt.xlabel("x (Prey Population)")
plt.ylabel("y (Predator Population)")
plt.legend()
plt.grid()
plt.show()

a, b, c, e, f, g = 0.5, 0.02, 0.01, 0.1, 0.1, 0.01

def predator_prey(t, vars):
    x, y = vars
    dx_dt = a * x - b * x**2 - c * x * y
    dy_dt = e * x * y + f * y - g * y**2
    return [dx_dt, dy_dt]

x_vals = np.linspace(0, 50, 20)
y_vals = np.linspace(0, 50, 20)
X, Y = np.meshgrid(x_vals, y_vals)

U = a * X - b * X**2 - c * X * Y
V = e * X * Y + f * Y - g * Y**2

magnitude = np.sqrt(U**2 + V**2)
U_norm = U / magnitude
V_norm = V / magnitude

t_span = (0, 200)
initial_conditions = [
    (10, 10),
    (20, 5),
    (5, 20),
    (30, 30)
]

plt.figure(figsize=(10, 6))
plt.quiver(X, Y, U_norm, V_norm, color="blue", alpha=0.6, label="Vector Field")

for x0, y0 in initial_conditions:
    sol = solve_ivp(predator_prey, t_span, [x0, y0], t_eval=np.linspace(0, 200, 1000))
    plt.plot(sol.y[0], sol.y[1], label=f"Trajectory from ({x0}, {y0})")

x_fixed = f / e
y_fixed = (a * e - b * f) / (c * e)
plt.scatter([0, x_fixed], [0, y_fixed], color="red", zorder=5, label="Fixed Points")

plt.title("Phase Plane for Predator-Prey System (Logistic Dynamics)")
plt.xlabel("Prey Population (x)")
plt.ylabel("Predator Population (y)")
plt.xlim(0, 50)
plt.ylim(0, 50)
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#part 3
t = np.linspace(0, 10, 500)
x0 = 0.0025
A = 6

x_approx1 = x0 * np.exp(-t / A)
x_approx2 = x0 * np.exp(-t)

plt.figure(figsize=(10, 6))
plt.plot(t, x_approx1, label='Approximation 1 (A >> x(t))')
plt.plot(t, x_approx2, label='Approximation 2 (A << x(t))', linestyle='--')
plt.title("Graphing Solution Curves")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.legend()
plt.grid(True)
plt.show()

#part 4
def euler_method(func, t0, x0, t_end, dt, K, A):
    t = [t0]
    x = [x0]
    while t[-1] < t_end:
        x_new = x[-1] + func(t[-1], x[-1], K, A) * dt
        t_new = t[-1] + dt
        t.append(t_new)
        x.append(x_new)
    return np.array(t), np.array(x)

def michaelis_menten(t, x, K, A):
    return -K * x / (A + x)

K = 1
A = 0.025
x0 = 0.025
t0 = 0
t_end = 10
dt = 0.01

t, x = euler_method(michaelis_menten, t0, x0, t_end, dt, K, A)

plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Direct Solution (Euler Method)')
plt.title("Solution Curve for Michaelis-Menten Equation")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.legend()
plt.grid(True)
plt.show()
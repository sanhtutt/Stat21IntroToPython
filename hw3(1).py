import numpy as np
import matplotlib.pyplot as plt

initial_plant_density = 3000
initial_deer_population = 100
time_steps = 30

plant_growth_rate = 0.8
deer_death_rate = 1.1

# Part I: Linear Interaction Model Simulation
plant_density_linear = [initial_plant_density]
deer_population_linear = [initial_deer_population]

for t in range(1, time_steps):
    P = plant_density_linear[-1]
    D = deer_population_linear[-1]
    new_plant_density = P + plant_growth_rate * P * (1 - P / 3000)
    new_deer_population = D - deer_death_rate
    
    plant_density_linear.append(new_plant_density)
    deer_population_linear.append(max(new_deer_population, 0))

# Part II: Caughley's Nonlinear Interaction Model Simulation
caughley_plant_coeff = 1.2
caughley_deer_coeff = 1.5
interaction_factor = 0.001

plant_density_nonlinear = [initial_plant_density]
deer_population_nonlinear = [initial_deer_population]

for t in range(1, time_steps):
    P = plant_density_nonlinear[-1]
    D = deer_population_nonlinear[-1]
    
    plant_interaction = caughley_plant_coeff * D * (1 - np.exp(-interaction_factor * P))
    deer_interaction = caughley_deer_coeff * D * (1 - np.exp(-interaction_factor * P))

    new_plant_density = P + plant_growth_rate * P * (1 - P / 3000) - plant_interaction
    new_deer_population = D - deer_death_rate + deer_interaction
    
    plant_density_nonlinear.append(max(new_plant_density, 0))
    deer_population_nonlinear.append(max(new_deer_population, 0))

# Part III: Plotting and Comparison
x_values = np.linspace(0, 5000, 100)
nonlinear_interaction_term = 1 - np.exp(-interaction_factor * x_values)

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(plant_density_linear, label='Linear Model', color='blue')
plt.plot(plant_density_nonlinear, label='Nonlinear Model', color='orange')
plt.title("Plant Density Over Time")
plt.xlabel("Time (years)")
plt.ylabel("Plant Density")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(deer_population_linear, label='Linear Model', color='blue')
plt.plot(deer_population_nonlinear, label='Nonlinear Model', color='orange')
plt.title("Deer Population Over Time")
plt.xlabel("Time (years)")
plt.ylabel("Deer Population")
plt.legend()

plt.subplot(2, 2, (3,4))
plt.plot(x_values, nonlinear_interaction_term, label='Nonlinear Interaction Term', color='green')
plt.title("Nonlinear Interaction Term (1 - exp(-0.001 * x))")
plt.xlabel("Plant Density (x)")
plt.ylabel("Interaction Strength")
plt.legend()

plt.tight_layout()
plt.show()

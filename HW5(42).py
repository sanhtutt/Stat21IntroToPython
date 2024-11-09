import numpy as np
import matplotlib.pyplot as plt

#(1)
initial_population = 100
birth_rate = 0.4
survival_rate = 0.68
years = 20
population_deterministic = [initial_population]
for year in range(1, years + 1):
    new_population = population_deterministic[-1] * birth_rate * survival_rate
    population_deterministic.append(population_deterministic[-1] + new_population)
plt.plot(range(years + 1), population_deterministic, label="Deterministic Model")
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Deterministic Model - Bobcat Population Over Time")
plt.legend()
plt.grid(True)
plt.show()

#(2)
birth_rate_mean = 0.4
birth_rate_sd = 0.1
survival_rate_mean = 0.68
survival_rate_sd = 0.07
runs = 50
populations_demographic = []
for run in range(runs):
    population = [initial_population]
    for year in range(years):
        birth_rate = np.random.normal(birth_rate_mean, birth_rate_sd)
        survival_rate = np.random.normal(survival_rate_mean, survival_rate_sd)
        new_population = population[-1] * birth_rate * survival_rate
        population.append(population[-1] + new_population)
    populations_demographic.append(population)
for population in populations_demographic:
    plt.plot(range(years + 1), population, color='gray', alpha=0.5)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Demographic Stochasticity - Bobcat Population Over Time")
plt.legend()
plt.grid(True)
plt.show()


#(3)
populations_environmental = []
for run in range(runs):
    population = [initial_population]
    for year in range(years):
        if np.random.rand() < 0.04:
            birth_rate = birth_rate_mean * 0.7
            survival_rate = survival_rate_mean * 0.7
        else:
            birth_rate = birth_rate_mean
            survival_rate = survival_rate_mean
        new_population = population[-1] * birth_rate * survival_rate
        population.append(population[-1] + new_population)
    populations_environmental.append(population)
for population in populations_environmental:
    plt.plot(range(years + 1), population, color='gray', alpha=0.5)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Environmental Stochasticity - Bobcat Population Over Time")
plt.legend()
plt.grid(True)
plt.show()

#(4)
end_year_demographic = [pop[-1] for pop in populations_demographic]
end_year_environmental = [pop[-1] for pop in populations_environmental]
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(end_year_demographic, bins=10, color='gray', edgecolor='black')
plt.title("Demographic Stochasticity - 20th Year Population")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.subplot(1, 2, 2)
plt.hist(end_year_environmental, bins=10, color='blue', edgecolor='black')
plt.title("Environmental Stochasticity - 20th Year Population")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
plt.boxplot([end_year_demographic, end_year_environmental], labels=["Demographic", "Environmental"])
plt.title("20th Year Population - Box Plot Comparison")
plt.ylabel("Population")
plt.show()

#(5)
demographic_10_years = [[pop[year] for pop in populations_demographic] for year in range(11)]
environmental_10_years = [[pop[year] for pop in populations_environmental] for year in range(11)]
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.boxplot(demographic_10_years, labels=range(11))
plt.title("Demographic Stochasticity - First 10 Years")
plt.xlabel("Years")
plt.ylabel("Population")
plt.subplot(1, 2, 2)
plt.boxplot(environmental_10_years, labels=range(11))
plt.title("Environmental Stochasticity - First 10 Years")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()
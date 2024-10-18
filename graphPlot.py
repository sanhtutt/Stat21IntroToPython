import csv
import matplotlib.pyplot as plt

years = []
age_25_34 = []
age_35_44 = []
age_45_54 = []
age_55_64 = []

with open('alcohol_induced_deaths.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        year = int(row[1])
        age_group = row[2]
        crude_rate = float(row[5])

        if age_group == '25-34 years':
            years.append(year)
            age_25_34.append(crude_rate)
        elif age_group == '35-44 years':
            age_35_44.append(crude_rate)
        elif age_group == '45-54 years':
            age_45_54.append(crude_rate)
        elif age_group == '55-64 years':
            age_55_64.append(crude_rate)

plt.plot(years, age_25_34, label='25-34 years')
plt.plot(years, age_35_44, label='35-44 years')
plt.plot(years, age_45_54, label='45-54 years')
plt.plot(years, age_55_64, label='55-64 years')

plt.xlabel('Year')
plt.ylabel('Crude Rate (per 100,000)')
plt.title('Alcohol-Induced Death Rate by Age Group (1999-2020)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

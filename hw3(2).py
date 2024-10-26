# Constants for the closed-form solution
lambda1, lambda2 = 0.87, 0.62
c1, c2 = -0.51999, 1.51999

# Recursive function to compute a(n) and b(n)
def recursive_a_b(n):
    a, b = 1, 1  # Initial values: a(0) = 1, b(0) = 1
    for _ in range(n):
        a, b = 0.87 * a + 0.38 * b, 0.62 * b
    return a, b

# Closed-form functions for a(n) and b(n)
def closed_form_a(n):
    return c1 * lambda1**n + c2 * lambda2**n

def closed_form_b(n):
    return lambda2**n

# Calculate the number of years for a(n) to reach 10% of initial level
n_years = 0
while True:
    a_recursive, _ = recursive_a_b(n_years)
    if a_recursive <= 0.1:  # 10% threshold
        break
    n_years += 1

print(f"It takes approximately {n_years} years for Lake Ontario's pollution to drop to 10% of its initial level.")
print(f"Recursive a({n_years}) = {recursive_a_b(n_years)[0]}")
print(f"Closed-form a({n_years}) = {closed_form_a(n_years)}")
print(f"Closed-form b({n_years}) = {closed_form_b(n_years)}")

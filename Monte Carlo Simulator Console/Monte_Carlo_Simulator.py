import numpy as np
import matplotlib.pyplot as plt

sim_quantity = int(input("Enter the number of simulations you wish to run: "))
min_val = float(input("Enter the minimum value of your range: "))
max_val = float(input("Enter the maximum value of your range: "))
target_val = float(input("Enter the target value of your range: "))

sim_result = np.random.uniform(min_val, max_val, sim_quantity)
plt.figure()
plt.hist(sim_result, density=True, edgecolor="white")
plt.axvline(target_val, color="r")
plt.show()

print((sim_result > target_val).sum() / sim_quantity)

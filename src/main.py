from spacecraft import spacecraft
from thermal import radiated_power
from sim import euler_solver

import matplotlib.pyplot as plt

sat = spacecraft(1000, 800, 10, 0.8) # disclaimer: these inputs are complete nonsense that I made up for testing purposes. I know the surface area of a cubesat is not 10 m^2.

electronic_power = 100 # W

temperature = 293

temperatures = []

for second in range(3600):

    temperature = euler_solver(
        sat,
        temperature,
        electronic_power,
        1
    )
    temperatures.append(temperature)

    print(second, temperature)

plt.plot(range(3600), temperatures)
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Cubesat Temperature Simulation')
plt.show()
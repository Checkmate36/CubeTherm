"""How much this thing radiates"""

from constants import stefan_boltzmann_constant

def radiated_power(spacecraft, temperature):
    return(spacecraft.emissivity * stefan_boltzmann_constant * spacecraft.area * temperature**4)

def net_power(spacecraft, temperature, electronic_power):
    return(electronic_power - radiated_power(spacecraft, temperature))

def dTdt(spacecraft, temperature, electronic_power):
    return(net_power(spacecraft, temperature, electronic_power) / (spacecraft.mass * spacecraft.specific_heat))
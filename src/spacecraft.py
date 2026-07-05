"""Spacecraft definition for modelling"""

class spacecraft:
    def __init__(self, mass, specific_heat, area, emissivity):
        self.mass = mass
        self.specific_heat = specific_heat
        self.area = area
        self.emissivity = emissivity
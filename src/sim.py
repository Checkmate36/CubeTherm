from thermal import dTdt

def euler_solver(spacecraft, temperature, electronics_power, dt):
    """Euler method for solving the differential equation for temperature change over time"""

    rate = dTdt(spacecraft, temperature, electronics_power)

    return temperature + rate * dt
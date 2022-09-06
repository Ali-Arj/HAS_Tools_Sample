import math

def air_pressure_at_height(h):
    p0 = 101325 #reference pressure in pascal
    M = 0.02896968 #molar mass of air kg/mol
    g = 9.81 #gravity m/s2  
    R0 = 8.314462618 #gas constant J/(mol.k)
    T= 273 #temp in kelvin

    ratio = -(g * h * M) / (R0 * T)
    p_h = p0 * math.exp(ratio)
    return p_h

#list of elevations to run
h_list = range(0, 1000, 100)
for h in h_list:
    p_h = air_pressure_at_height(h)
    print(h, '     ', p_h)

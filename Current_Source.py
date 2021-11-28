import math

Iref = 5 * 1e-6
K_n = 181 * 1e-6
K_p = 48 * 1e-6
Von = 0.3

sn = 2 * Iref / (K_n * Von ** 2)
sp = 2 * Iref / (K_p * Von ** 2)
sn = math.ceil(sn)
sp = math.ceil(sp)

print(sn, sp)

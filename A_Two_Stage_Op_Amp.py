# Easy implementation just for calculating
import math

# known parameters
K_n = 181 * 1e-6
K_p = 48 * 1e-6
Vth_n = 0.695
Vth_p = 0.672
Vth_o = 0.15 # worst threshold offset
lamda_n = 0.037
lamda_p = 0.008
C_ox = 3.9 * 8.854 * 1e-12 / (6.65 * 1e-9)

# standards
C_L = 10 * 1e-12
Av = 10000
VDD = 3.3
GB = 5 * 1e6
SR = 6 / 1e-6
Vout_min = 0.5
Vout_max = 2.5
Vin_min = 1.25
Vin_max = 2.5
P_diss = 2 * 1e-3

# calculating process

Cc = (math.ceil(3.2) / 10) * C_L
I5 = Cc * SR
S3 = (2 * 0.5 * I5) / (K_p * (VDD - Vout_max - (Vth_n + Vth_o) + (Vth_p - Vth_o)) ** 2)
S3 = math.ceil(S3)
S4 = S3

# here not write p3
gm3 = (2 * K_p * S3 * (0.5 * I5)) ** 0.5
# here not write p3

gm1 = GB * Cc * 2 * math.pi
S1 = gm1 ** 2 / (2 * K_n * (0.5 * I5))
S1 = math.floor(S1)
S2 = S1

Von5 = Vin_min - (2 * (0.5 * I5) / ((K_n * S1))) ** 0.5 - (Vth_n + Vth_o)
S5 = 2 * I5 / (K_n * Von5 ** 2)
S5 = math.ceil(S5)

gm6 = 18 * gm1
gm4 = gm3
S6 = S4 * gm6 / gm4
S6 = math.ceil(S6)

I6 = gm6 ** 2 / (2 * K_p * S6)
print(I5, I6)
S7 = I6 / I5 * S5
S7 = math.ceil(S7)

print(S1, S2, S3, S4, S5, S6, S7)

print(Cc)
print(I5)
av = 2 * gm1 * gm6 / (I5 * (lamda_n+lamda_p) * I6 * (lamda_n+lamda_p))
print(av)
pdiss = (I5 + I6) * 3.3
print(pdiss)
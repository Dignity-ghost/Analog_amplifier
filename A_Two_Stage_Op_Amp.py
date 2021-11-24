# Easy implementation just for calculating
import math

# known parameters
K_n = 120 * 1e-6
K_p = 25 * 1e-6
Vth_n = 0.5
Vth_p = 0.5
Vth_o = 0.15 # worst threshold offset
lamda_n = 0.06
lamda_p = 0.08
C_L = 10 * 1e-12
C_ox = 6 * 10-15

# standards
Av = 3000
VDD = 2.5
GB = 5 * 1e6
SR = 10 / 1e-6
Vout_min = 0.5
Vout_max = 2
Vin_min = 1.25
Vin_max = 2
P_diss = 2 * 1e-3

# calculating process

Cc = (math.ceil(2.2) / 10) * C_L
I5 = Cc * SR
S3 = (2 * 0.5 * I5) / (K_p * (VDD - Vout_max - (Vth_n + Vth_o) + (Vth_p - Vth_o)) ** 2)
S3 = round(S3)
S4 = S3

# here not write p3
gm3 = (2 * K_p * S3 * (0.5 * I5)) ** 0.5
# here not write p3

gm1 = GB * Cc * 2 * math.pi
S1 = gm1 ** 2 / (2 * K_n * (0.5 * I5))
S1 = math.ceil(S1)
S2 = S1

Von5 = Vin_min - (2 * (0.5 * I5) / ((K_n * S1))) ** 0.5 - (Vth_n + Vth_o)
S5 = 2 * I5 / (K_n * Von5 ** 2)
S5 = math.ceil(S5)

gm6 = 10 * gm1
gm4 = gm3
S6 = S4 * gm6 / gm4
S6 = math.ceil(S6)

I6 = gm6 ** 2 / (2 * K_p * S6)
S7 = I6 / I5 * S5
S7 = math.ceil(S7)

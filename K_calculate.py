import numpy as np
import math

#n33
# vg1 = 1.2
# vg2 = 1.8
# vd1 = 2.1
# vd2 = 3.0
# i11 = 31.4808 * 1e-6
# i12 = 132.805 * 1e-6
# i21 = 32.4505 * 1e-6
# i22 = 134.752 * 1e-6
#p33
vg1 = 1.2
vg2 = 1.5
vd1 = 1.5
vd2 = 2.1
i11 = 26.2476 * 1e-6
i12 = 42.8322 * 1e-6
i21 = 27.3797 * 1e-6
i22 = 43.9709 * 1e-6

## test on website
# vg1 = 0.8
# vg2 = 1.0
# vd1 = 1.0
# vd2 = 1.5
# i11 = 28.62 * 1e-6
# i12 = 53.72 * 1e-6
# i21 = 30.35 * 1e-6
# i22 = 56.21 * 1e-6
# vg1 = 0.8
# vg2 = 1.0
# vd1 = 1.0
# vd2 = 1.5
# i11 = 12.83 * 1e-6
# i12 = 23.47 * 1e-6
# i21 = 13.33 * 1e-6
# i22 = 24.02 * 1e-6


lamda = (i21 - i11) / (i11*vd2 - i21*vd1)
print(lamda)
vth = (np.sqrt(i12/i11) * vg1 - vg2) / (np.sqrt(i12/i11) - 1)
print(vth)
k = i11 / ((vg1 - vth) ** 2 * (1 + lamda * vd1))
print(k)
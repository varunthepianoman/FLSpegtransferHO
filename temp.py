import numpy as np

conv = np.array([180, 184, 176, 141, 185, 202, 178, 146, 190, 206, 193])*0.01
new = np.array([213, 205, 202, 177, 225, 215, 207, 177, 220, 218, 227])*0.01
print ((new - conv))
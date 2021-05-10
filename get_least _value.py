import numpy as np
from scipy import stats

data = np.array([4, 5, 1, 2, 7, 2, 6, 9, 3])
dt_mean = np.mean(data)
dt_median = np.median(data)
dt_mode = stats.mode(data)

print(round(dt_mean, 2))
print(dt_median)
print(dt_mode[0][0])



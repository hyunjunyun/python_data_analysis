from statistics import variance, stdev
import numpy as np

game_points = np.array([35, 56, 43, 59, 63, 79, 35, 41, 64, 93])

q75, q25 = np.percentile(game_points, [75, 25])

print(
    q25, q75, sep=" ")

print("Inter quartile range : ", q75 - q25)

from scipy.fft import fft
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def avg(arr):
    sum = np.zeros((256,), dtype=int)
    for i in range(len(arr)):
        sum = np.add(sum, arr[i])
    return sum / len(arr)


array = []
dispersion = []
data = pd.read_csv("ch00_B0833-45_20150612_191438_010_4.txt", sep=" ", header=None)[0]

for i in range(0, round(len(data) / (512 * 10))):
    array.append(
        avg(
            [
                [
                    np.abs(point)
                    for point in np.array_split(
                        fft([data[j] for j in range(k * 512, (k + 1) * 512)]),
                        2,
                    )[0]
                ]
                for k in range(i * 10, (i + 1) * 10)
            ]
        )
    )

array = np.transpose(array)
plt.xlabel("time(ms)")
plt.ylabel("frequency(MHz)")
plot = plt.imshow(array, cmap="Spectral", aspect="auto")
plt.colorbar(plot)
plt.show()
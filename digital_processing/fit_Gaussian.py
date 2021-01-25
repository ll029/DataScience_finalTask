import numpy as npy
import matplotlib.pyplot as plt
from scipy.stats import norm

f = open('.\\data', 'r+', encoding='utf-8')
data_list = f.readlines()
for i in range(0, len(data_list)):
    data_list[i] = int(data_list[i])

x = npy.array(data_list)

mu = npy.mean(x)
sigma = npy.std(x)
num_of_bins = 300
n, bins, patches = plt.hist(x, num_of_bins, density=1, alpha=1)
y = norm.pdf(bins, mu, sigma)

plt.grid(True)
plt.plot(bins, y, 'r--')
plt.xlabel('sum_threeValue')
plt.ylabel('Probability')
plt.title('Histogram : $\mu$=' + str(round(mu, 2)) + ' $\sigma=$' + str(round(sigma, 2)))
plt.show()

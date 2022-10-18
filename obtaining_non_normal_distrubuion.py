import numpy as np
import matplotlib.pyplot as plt
# an example of a distribution that is not going to be normal is the distribution of
# sample_proportion when multiple samples is drawn out of a population to estimate the population mean if:
# n(1-p) or np are less than ten, where n is the number of individual in each sample,
# p is the population proportion
a = np.random.randint(0, 2, 1000)  # 1000 coin toss a.mean() should be around 50%(fair coin)


def generate_unfair_coin(p, tosses) :
    lst1 = int(np.ceil(p * tosses)) * [1]
    lst0 = int(np.ceil((1 - p) * tosses) - 1) * [0]
    lst = lst1 + lst0
    indx = np.random.randint(0, tosses - 1, tosses)
    shuffeledlist = []
    for i in range(tosses) :
        thisiterindx = indx[i]
        shuffeledlist.append(lst[thisiterindx])
    return np.array(shuffeledlist)


def random_sampler(population, n) :
    sample = []
    zz = np.random.randint(0, len(population) - 1, n)
    for k in zz :
        sample.append(population[k])
    return sample


def generate_some_samples(numberofsamples, coin) :  # draw some sample of 50 tosses out of this population
    matrix_of_50_samples = np.zeros([50, numberofsamples])
    for j in range(50) :
        matrix_of_50_samples[j, :] = random_sampler(coin, numberofsamples)
    lst_of_sample_proportions = []
    for i in range(50) :
        proportion_of_each_sample = matrix_of_50_samples[i, :].sum() / numberofsamples
        lst_of_sample_proportions.append(proportion_of_each_sample)
    plt.plot(lst_of_sample_proportions)
    return lst_of_sample_proportions


# here the  distribution is that of the sample population
# (when we have many samples, what would be the shape of distribution of each one's proportion)
# the safety rule says that if the samples number is low or if the proportion is close to one or close to zero
# that the distributing of the samples proportion would not be normal
# the rule is np and n(1-p) should be both larger than 10
# n is the number of samples (the first argument of: generate_some_samples(numberofsamples, coin)
# and p is the population proportion (the first argument of generate unfair coin

a = generate_unfair_coin(.5, 10000)
data = generate_some_samples(15, a)

# Example of the Shapiro-Wilk Normality Test
# Observations in each sample are independent and identically distributed (iid).

from scipy.stats import shapiro
# data = []
stat, p = shapiro(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05 :
    print('Probably Gaussian')
else :
    print('Probably not Gaussian')
# plt.plot(data)


# Example of the D'Agostino's K^2 Normality Test
from scipy.stats import normaltest

# data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]

stat, p = normaltest(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05 :
    print('Probably Gaussian')
else :
    print('Probably not Gaussian')

import matplotlib.pyplot as plt
# plt.plot(data)

# Example of the Anderson-Darling Normality Test
from scipy.stats import anderson

# data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
# data=10 * [10]
result = anderson(data)
print('stat=%.3f' % (result.statistic))

for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < cv :
        print('Probably Gaussian at the %.1f%% level' % (sl))
    else :
        print('Probably not Gaussian at the %.1f%% level' % (sl))
plt.plot(data)
plt.show()
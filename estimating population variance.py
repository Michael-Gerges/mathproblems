import numpy as np

# from keras.models import Sequential


population = 100 * np.random.random(10000)
print(population[30 :80])
print(np.array(population).std())


def cal_variance(listofnumbers) :
    mean = np.array(listofnumbers).mean()
    summutionlist = []
    for i in range(len(listofnumbers)) :
        nominator = (listofnumbers[i] - mean) ** 2
        summutionlist.append(nominator)
    variance = sum(summutionlist) / len(listofnumbers)
    return variance


popvar = cal_variance(population)

list_of_variance = []


def sampler(samplesize) :
    sampler = []
    index_of_population = int(np.random.randint(0, len(population)))
    sampler.extend(population[index_of_population :index_of_population + samplesize])
    variance = cal_variance(sampler)
    list_of_variance = []
    for j in range(1000) :
        list_of_variance.append(variance)
    meanofvarianceat = np.array(list_of_variance).mean()
    ratio = popvar / meanofvarianceat

    return 1 / ratio


for i in range(20, 30) :
    print('at sample size = ', i, 'the ratio equals', sampler(i), 'while the unbiased ratio is', (i - 1) / i)













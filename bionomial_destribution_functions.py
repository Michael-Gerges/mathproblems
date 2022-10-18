import random
import math
import numpy as np

memory = {}


def fact(n) :  # O(n) = x^n
    if n <= 1 :  # base case
        memory[n] = 1
        return memory[n]
    #print(memory)
    memory[n] = n * fact(n - 1)
    #print(memory)
    return math.gamma(n+1) # memory[n]  # ladder


def choose(trials, successes) :
    ''' let nCk be n choose k where n = trials and k = successess'''
    return fact(trials) / (fact(trials - successes) * fact(successes))


def Binomial_Probability_distribution_function(trials, successes, probability_of_success) :
    return (choose(trials, successes)) * (probability_of_success ** successes) * (
                (1 - probability_of_success) ** (trials - successes))


def Binomial_probiility_density_function(trials, successes, probability_of_success) :
    lst = []
    for i in range(successes + 1) :
        lst.append(Binomial_Probability_distribution_function(trials, i, probability_of_success))
    return sum(lst)


def mean_binomial(trials, probability_of_sucess) :
    return trials * probability_of_sucess


def variance_binomial(trials, probability_of_success) :
    return trials * probability_of_success * (1 - probability_of_success)


# print(Binomial_probiility_density_function(20, 5, .95)*100, '%')  # a meta-analysis of 20 trials 5 of which are incorrect

# print(choose(4, 2))

# print(Binomial_Probability_distribution_function(100, 100, .5))

# print(choose(100, 40))


def Stirlingsapproximation(n) :
    firstterm = np.sqrt(2 * np.pi * n)
    secondterm = (n / np.e) ** n
    return firstterm * secondterm


##  overflow encountered:

x = np.arange(1, 100, 1)
y = []

for i in x :
     # y.append(math.gamma(i+1)/6**i)
     print("for ", i, "the gamma is ",math.gamma(i+1), "my function is ", fact(i) )


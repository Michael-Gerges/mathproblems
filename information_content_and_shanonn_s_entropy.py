import math
import numpy as np
import matplotlib.pyplot as plt
import random




def shannon_content(p):
    """
we want to know the information content in bits so we take log base 2
so the units is bits per symbol
the information generated by the occurrence of an instance with probability p
for example one bit per symbol is generated by a fare coin flip
if the coin is 0.6 chance tail then a tail will generate 0.7369 bits and a head will generate 1.3219 bits
the entropy (the average information generated wighted by probability of occurrence is 0.9709 compared to a fair coin
which has the maximal entropy 1
    """
    if p == 0 or p == 1:
        return 0
    return math.log(1/p, 2)


def entropy(p):  # takes lists, floats, or ints
    arg_type = str(type(p))
    if arg_type == "<class 'float'>" or arg_type == "<class 'float'>":
        """
    in bits per symbol, in the special case that it is the outcome of 2 outcome variable with probabilities p and 1-p
        """
        return (p*shannon_content(p) + (1-p)*shannon_content(1 - p))
    elif arg_type == "<class 'list'>":
        if sum(p) != 1:
            raise ValueError("this is not valid probability distribution, its not adding up to 1")
        answer_list = []
        for i in range(len(p)):  # len(p) is the number of characters
            answer_list.append(p[i]*shannon_content(p[i]))
        # return - sum(answer_list)
        return sum(answer_list)
    else:
        raise TypeError('expected data type is a probability or a probability vector')

# x = [i for i in np.linspace(0, 1, 20)]
# y = [entropy(i) for i in x]
# 
# # Data for plotting
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set(xlabel='proability (s)', ylabel='entropy (bits/symbol)',
#        title='About as simple as it gets, folks')
# 
# ax.grid()
# fig.savefig("test.png")
# plt.show()


probabilities1 = [.5, .25, .145, .105]  # for expermination
probabilities2 = [0.25, 0.25, 0.25, 0.25]  # equioproable list of events
probabilities3 = [.5, .25, .125, .125]
alphabet = ["a", "b", "c", "d"]  # 4 litters alphabet

source_code1 = {}
source_code2 = {}
for i in range(len(alphabet)):
    source_code1[alphabet[i]] = np.binary_repr(int((1 / probabilities1[i]) - 1))

for i in range(len(alphabet)):
    source_code2[alphabet[i]] = np.binary_repr(int((1 / probabilities2[i]) - 1))


def expected_len(sourcecode, probabilities):
    i = 0
    lst = []
    for key in sourcecode:
        lst.append(int(len(sourcecode[key])) * probabilities[i])
        i += 1
    return sum(lst)


def alphabet_generator(n):
    string = "The fundamental step in communications, including communications at the molecular level, " \
             "is the accurate reception of a signal." \
             " As is well known in communications engineering fields, the mathematical" \
             " foundation for obtaining good reception was developed by Claude Shannon in 1948 and 1949 [55–57]." \
             " How can we apply these ideas to the construction" \
             " of molecular communications?" \
             " One approach is to first find out how biomolecules interact with each other and how they set " \
             "their states. With some changes in perspective from conventional biochemistry, " \
             "the states and patterns of molecules can be measured by using information theory" \
             " and the field of study can be called molecular information theory"
    lst = []
    while len(lst) < n:
        index = random.randint(0, len(string))
        if string[index] in lst:
            continue
        elif str(string[index]) == ' ' or str(string[index]) == ',':
            continue
        else:
            lst.append(string[index])
    return lst


def probability_generator(any_alphabet):
    """generate probabilities in the form 0.5 0.25 0.125 0.0625 ... summing up to 1"""
    probability2 = []
    for i in range(1, len(any_alphabet) + 1):
        if i == len(any_alphabet):
            probability2.append(1 - sum(probability2))
        else :
            probability2.append(1 / (2 ** i))
    return probability2


def coder(any_alphabet):
    """maps alphabet to a code which length is binary of inverse the probability
    for example: a character with a probability 0.5  will coded with one binary character
    but a character with probability 0.25 will be coded with 2 binary characters
    """
    source_code = {}
    probabilities = probability_generator(any_alphabet)

    for i in range(len(any_alphabet)):
        source_code[any_alphabet[i]] = np.binary_repr(int((1 / probabilities[i]) - 1))
    return source_code


def cost_of_code(sourcecode):
    """ preserved quantity lurking in the unique decodability "to be less than or equal to 1 Kraft-inequality"""
    lst = []  # list for the cost of every code in the source code,
    # the more the length of the code the less its cost
    # so the codes that are very short like one bit long such as a zero or a one will have a cost of 0.5
    # that's why they miss up with unique decodability
    # they are  expensive to pick in regards to unique decodablity
    # that's sad because  they are capable of reducing the expected code length
    # if the cost exceed 1 we are guaranteed that we violated unique decodablity
    # if the cost is less than one that means we can have shorter expected length by utilizing the shorter codes
    # and adding up to the cost until it hits one
    # a code with cost of one is complete code
    for key in sourcecode:
        lst.append(2 ** (-int(len(sourcecode[key]))))
    return sum(lst)


def ideal_length(any_probabilities):
    """ takes probability vector
    for optimal code the ideal length of any character is shanon information content"""
    lst = []
    for i in range(len(any_probabilities)):
        lst.append(math.log(1/any_probabilities[i], 2))
    return lst

six_alphabet = alphabet_generator(6)
six_probability = probability_generator(six_alphabet)
# six_code = (coder(six_alphabet))
# print("my alphabet is ", six_alphabet)
# print('the probabilities of each character of the alphabet is ',six_probability)
# print('my code is ', six_code)
# print("the entropy of the code is ", entropy(six_probability))
# print('the expected length is ', expected_len(six_code, six_probability), 'note: if it is equal to the entropy, so the code is optimal')
# print("the ideal length of each caracter should be ", ideal_length(six_probability))
# print("the cost of code = ", cost_of_code(six_code), " note: if it is 1, so the code is optimal")


def optimal_coder(lst):  # takes probability vector (hulfman algorism)
    original_list = tuple(lst)
    mapp = {}

    def coding(lst):
        # print(original_list)
        if len(lst) > 1:
            lst.sort()
            lst.reverse()
            smallest_probabilities = []
            smallest_probabilities = [lst.pop(), lst.pop()]
            # print(smallest_probabilities)
            # count = 0
            for i in range(2):
                # count += 1
                # print(i)
                if smallest_probabilities[i] in original_list:
                    mapp[smallest_probabilities[i]] = np.binary_repr(int((1 / smallest_probabilities[i]) - 1))
                    # mapp[smallest_probabilities[i]] = math.log(1/smallest_probabilities[i], 2)
                    # mapp[smallest_probabilities[i]] = np.binary_repr(count)
            lst.append(sum(smallest_probabilities))
            coding(lst)
            return mapp
    coding(lst)
    return mapp


print(coder(six_probability))
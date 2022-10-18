import numpy

import time
print(time.time())
a = [i for i in range(10000)]
b = [i for i in range(10000)]

tic = time.time()
dot = 0.0

for i in range(len(a)):
    dot += a[i] * b[i]

toc = time.time()

print("dot_product = " + str(dot))
print("Computation time = " + str(1000*(toc - tic)) + " ms")


n_tic = time.time()
n_dot_product = numpy.array(a).dot(numpy.array(b))
n_toc = time.time()

print("\nn_dot_product = "+str(n_dot_product))
print("Computation time = "+str(1000*(n_toc - n_tic))+" ms")

c = numpy.arange(10, 12, .1)
d = numpy.arange(10, 12, .1)

# print(numpy.vstack((c,d)))
# print(numpy.hstack((c,d)))
# print(numpy.dstack((c,d)))

# print(numpy.dstack.__doc__)

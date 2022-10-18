def fact(n):         # O(n) = x^n
    if n <= 1:                       # base case
        return 1
    return n * fact(n - 1)           # ladder


print(fact(100))

# print(fact(10))

# memo = {}
# def fib(n):             # memorize 
#     if n in memo:
#         return memo[n]
#
#     if n <= 2:
#         return 1
#     else:
#         f = fib(n-1) + fib(n-2)
#     memo[n] = f
#     return f
#
#
# print(fib(17))
# print(type(memo))


def fib_BottomUp(n):        # to slow
    fib = {}
    for k in range(1, n + 1):
        if k <= 2:
            f = 1
        else:
            f = fib_BottomUp(n - 1) + fib_BottomUp(n - 2)
        fib[k] = f
    return fib[n]


print(fib_BottomUp(11))

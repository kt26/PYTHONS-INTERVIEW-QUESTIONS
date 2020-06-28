def memoize(function):
    cache = {}
    def helper(x):
        if x not in cache:            
            cache[x] = function(x)
        return cache[x]
    return helper
    

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)


print(fib(499))






""" STILL BEST SOLUTION IS THIS """

# def fib(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         b = a+b
#         a = b-a
#     return a

# print(fib(100000))
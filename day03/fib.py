
def fun1(arg):
    # global x
    # do smth
    print(arg)
    arg = 5
    # x is only defined inside of fun1
    return arg

def fun2rec(count):
    if count > 5:
        return
    print(' '*count + 'in', count)
    fun2rec(count+1)
    print(' '*count + 'out', count)
    # return None

# x = 1
# a = fun1("hello")
# a = fun1(x)
# print('a here', a)
fun2rec(0)

def mysum(n):
    if n == 0:
        return 0
    # sum of 1..n
    # assuming we know sum 1..n-1
    x = mysum(n-1)  # sum 1 .. n-1
    val = x + n
    return val




# write a function that computes the nth fibonacci number

def fib(n):
    ...
    return None

# 0 1 2 3 4 5 6 < indices
# 0 1 1 2 3 5 8 < values



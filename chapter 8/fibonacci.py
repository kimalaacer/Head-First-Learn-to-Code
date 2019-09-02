import time

cache={}
def fibonacci(n):
    global cache
    if n in cache:
        return cache[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        result= fibonacci(n-1)+fibonacci(n-2)
    cache[n]=result
    return result
start=time.time()
for n in range(0,101):
    result=fibonacci(n)
    print(n, result)
end=time.time()
duration=end-start
print('computed all 100 Fibonacci numbers in', duration, 'seconds')

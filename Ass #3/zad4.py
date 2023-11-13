import functools
def pamiec(func):
 dictionary = {}
 @functools.wraps(func)
 def wrapper(*args, **kwargs):
     if args in dictionary:
         return dictionary[args]
     else:
         result = func(*args, **kwargs)
         dictionary[args] = result
         return result

 return wrapper

@pamiec
def fibonacci(n):
 return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
for i in range(100):
 print(fibonacci(i))
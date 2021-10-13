from functools import wraps

def count_calls(f):
    wraps(f)
    def helper(*args, **kwargs):
        helper.call_count += 1
        return f(*args, **kwargs)
        
    helper.call_count = 0
    return helper

@count_calls
def add(a,b):
    return a + b

def counter():
    for i in range(123):
        print(add(i, i+1))
    
    print(f"Function was called {add.call_count} times.")
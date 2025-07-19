'''
def greet(name):
    print(f"Hello, {name}")
    
greet("Alice")  

def add(a, b):
    return a + b

result = add(2, 5)
print(result)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

result = factorial(2)    #this line ensures that the result of the function can be printed
print(f"the factorial is {result}")

def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")
    
greet("Bob", "Good morning")    

    

   
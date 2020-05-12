def factorial(x):
    assert x>=0, "Enter a positive number"
    assert round(x)== x, "Enter an integer"
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(5))
print(factorial(-5))

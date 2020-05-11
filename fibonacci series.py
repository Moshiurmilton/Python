def get_fib(n):
    p = 0
    q = 1
    if n <= 0:
        print("Enter a valid number:")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for x in range(2, n):
            r = p + q
            p = q
            q = r
        return q
print(get_fib(11))

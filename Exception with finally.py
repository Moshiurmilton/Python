try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Error: Division by Zero not possible.")
finally:
    print([1, 2, 3, 4, 5, 6])

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Python Calculator")
    print("10 + 20 =", add(10, 20))
    print("20 - 5 =", subtract(20, 5))
    print("5 * 4 =", multiply(5, 4))
    print("20 / 4 =", divide(20, 4))
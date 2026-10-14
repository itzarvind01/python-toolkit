
"""Interactive calculator with input validation and calculation history."""

import math


def calculate(a, operator, b):
    """Perform a mathematical operation."""
    operations = {
        "+": lambda: a + b,
        "-": lambda: a - b,
        "*": lambda: a * b,
        "/": lambda: a / b,
        "%": lambda: a % b,
        "**": lambda: a ** b,
    }

    if operator not in operations:
        raise ValueError("Unsupported operator")

    if operator == "/" and b == 0:
        raise ValueError("Cannot divide by zero")

    if operator == "%" and b == 0:
        raise ValueError("Cannot calculate modulo zero")

    result = operations[operator]()

    if not math.isfinite(result):
        raise ValueError("Result is too large or invalid")

    return result


def main():
    history = []

    print("=== Python Toolkit Calculator ===")
    print("Operators: +  -  *  /  %  **")
    print("Type 'history' to view calculations.")
    print("Type 'exit' to quit.")

    while True:
        command = input("\nEnter calculation: ").strip()

        if command.lower() == "exit":
            print("Goodbye!")
            break

        if command.lower() == "history":
            if not history:
                print("No calculations yet.")
            else:
                for item in history:
                    print(item)
            continue

        try:
            parts = command.split()

            if len(parts) != 3:
                print("Use this format: 10 + 5")
                continue

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            result = calculate(a, operator, b)
            entry = f"{a:g} {operator} {b:g} = {result:g}"

            history.append(entry)
            print("Result:", result)

        except ValueError as error:
            print("Invalid calculation:", error)


if __name__ == "__main__":
    main()

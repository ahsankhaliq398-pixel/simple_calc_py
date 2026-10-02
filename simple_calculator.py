import operator

# Pre-mapped operator lookup for O(1) execution time
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(num1: float, op: str, num2: float):
    action = OPERATIONS.get(op)
    if not action:
        return "Error: Invalid operator. Supported: +, -, *, /"
    
    if op == '/' and num2 == 0:
        return "Error: Division by zero is undefined."
    
    return action(num1, num2)

def main():
    print("Simple Calculator (Type 'q' to quit)")
    
    while True:
        raw = input("\nEnter calculation (e.g., 5 + 3): ").strip()
        if raw.lower() == 'q':
            print("Goodbye!")
            break

        tokens = raw.split()
        if len(tokens) != 3:
            print("Error: Format must be: <number> <operator> <number>")
            continue

        try:
            num1 = float(tokens[0])
            op = tokens[1]
            num2 = float(tokens[2])
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        result = calculate(num1, op, num2)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
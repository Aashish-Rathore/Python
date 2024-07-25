class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

# Example usage
calc = Calculator()
print("Addition: 3 + 5 =", calc.add(3, 5))
print("Subtraction: 10 - 4 =", calc.subtract(10, 4))
print("Multiplication: 6 * 7 =", calc.multiply(6, 7))
print("Division: 8 / 2 =", calc.divide(8, 2))
print("Division: 8 / 0 =", calc.divide(8, 0))

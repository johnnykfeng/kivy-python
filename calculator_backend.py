class Calculator:
    @staticmethod
    def add(x, y):
        return float(x) + float(y)

    @staticmethod
    def subtract(x, y):
        return float(x) - float(y)

    @staticmethod
    def multiply(x, y):
        return float(x) * float(y)

    @staticmethod
    def divide(x, y):
        if float(y) == 0:
            return "Error: Division by zero"
        return float(x) / float(y)

    @staticmethod
    def calculate(operation, x, y):
        operations = {
            '+': Calculator.add,
            '-': Calculator.subtract,
            '*': Calculator.multiply,
            '/': Calculator.divide
        }

        if operation in operations:
            return operations[operation](x, y)
        return "Invalid operation"

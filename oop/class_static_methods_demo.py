class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method - does not require access to the class or instance
    @staticmethod
    def add(a, b):
        return a + b

    # Class method - accesses class-level data through 'cls'
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

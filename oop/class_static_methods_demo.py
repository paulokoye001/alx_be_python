class Calculator:
    """A Calculator class demonstrating class methods and static methods."""
    
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """A static method to perform addition."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """A class method to perform multiplication and reference a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

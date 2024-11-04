class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):
            result = self.add(result, a)
        if (b < 0): result = -result
        return result

    def divide(self, a, b):
        result = 0
        a_abs, b_abs = abs(a), abs(b)
        while a_abs >= b_abs:
            a_abs = self.subtract(b_abs, a_abs)
            result += 1
        if (a < 0) != (b < 0):
            result = -result
        return result
    
    def modulo(self, a, b):
        x=a<0
        a = abs(a)  # Work with absolute value of a
        b = abs(b)  # Work with absolute value of b
        while a >= b:
            a -= b  
        if x:
            a = - a
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
class Calculator:
    """This class contains methods for basic arithmetic operations"""

    @staticmethod
    def _add(num1, num2):
        """This function adds two numbers"""

        return num1 + num2

    @staticmethod
    def _subtract(num1, num2):
        """This function subtracts two numbers"""

        return num1 - num2

    @staticmethod
    def _multiply(num1, num2):
        """This function multiplies two numbers"""

        return num1 * num2

    @staticmethod
    def _divide(num1, num2):
        """This function divides two numbers"""

        if num2 == 0:
            return "Error: Division by zero"
        return round(num1 / num2, 2)

    _operations = {
        "+": _add,
        "-": _subtract,
        "*": _multiply,
        "/": _divide
    }

    @staticmethod
    def calculator(num1):
        while True:
            choice_of_operation = input(f"Pick an operation (+ , -, *, /): ")
            if choice_of_operation  not in Calculator._operations:
                print("Invalid operation. Please try again.")
                continue
            
            if num1 is None:
                num1 = float(input("Enter the first number: "))
            else:
                print(f"First number: {num1}")
            num2 = float(input("Enter the second number: "))

            calculation_function = Calculator._operations[choice_of_operation]
            result = calculation_function(num1, num2)

            while True:
                choice = input(f"Type 'y' to continue calculating with the {result} or 'n' to exit: ").lower()
                if choice == 'n':
                    print("Goodbye!")
                    exit()
                elif choice == 'y':
                    num1 = result
                    break
                else:
                    print("Invalid choice. Please enter 'y' or 'n'.")

Calculator.calculator(None)
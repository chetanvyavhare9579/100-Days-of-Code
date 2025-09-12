import math

def calculator():
    print("Professional Python Calculator")
    print("----------------------------------")
    print("Operations Available:")
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")
    print("5. % Modulus")
    print("6. x² Square")
    print("7. √ Square Root")
    print("8. ^ Power")
    print("9. ! Factorial")
    print("10. log Logarithm (base 10)")
    print("11. sin(x) in degrees")
    print("12. cos(x) in degrees")
    print("13. tan(x) in degrees")
    print("14. ❌ Exit")

    while True:
        try:
            choice = int(input("\nEnter choice (1-14): "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1-14.")
            continue

        if choice == 14:
            print("👋 Exiting Calculator. Goodbye!")
            break

        try:
            if choice in [1, 2, 3, 4, 5, 8]:  # operations needing two inputs
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            elif choice in [6, 7, 9, 10, 11, 12, 13]:  # single input operations
                num1 = float(input("Enter number: "))

            # Perform operations
            if choice == 1:
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"Result: {num1} × {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("❌ Error! Division by zero not allowed.")
                else:
                    print(f"Result: {num1} ÷ {num2} = {num1 / num2}")
            elif choice == 5:
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif choice == 6:
                print(f"Result: {num1}² = {num1 ** 2}")
            elif choice == 7:
                if num1 < 0:
                    print("❌ Error! Cannot find square root of a negative number.")
                else:
                    print(f"Result: √{num1} = {math.sqrt(num1)}")
            elif choice == 8:
                print(f"Result: {num1} ^ {num2} = {math.pow(num1, num2)}")
            elif choice == 9:
                if num1 < 0 or not num1.is_integer():
                    print("❌ Error! Factorial only works for non-negative integers.")
                else:
                    print(f"Result: {int(num1)}! = {math.factorial(int(num1))}")
            elif choice == 10:
                if num1 <= 0:
                    print("❌ Error! Logarithm is only defined for positive numbers.")
                else:
                    print(f"Result: log10({num1}) = {math.log10(num1)}")
            elif choice == 11:
                print(f"Result: sin({num1}°) = {math.sin(math.radians(num1))}")
            elif choice == 12:
                print(f"Result: cos({num1}°) = {math.cos(math.radians(num1))}")
            elif choice == 13:
                print(f"Result: tan({num1}°) = {math.tan(math.radians(num1))}")
            else:
                print("⚠️ Invalid choice! Please select a valid option.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    calculator()


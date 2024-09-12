'''
### Explanation:

1. **Function Definition**: The program defines a function `calculate_total_bill()` that encapsulates the entire logic.

2. **User Input**:
   - It prompts the user to input the number of coffee cups using `int(input(...))`. The program expects an integer input.
   - It similarly prompts for the price per coffee cup using `float(input(...))` to allow for decimal values, representing the monetary value more accurately.

3. **Validation**:
   - The program includes checks to ensure that neither the quantity nor the price per cup is negative. If negative values are entered, a `ValueError` is raised.

4. **Calculation**:
   - The total bill is calculated by multiplying the quantity of cups by the price per cup.

5. **Output**:
   - The total bill is outputted to the console, formatted to two decimal places for clarity using formatted string literals (f-strings).

6. **Exception Handling**:
   - The program includes a `try-except` block to catch and handle any `ValueError` exceptions that may arise from invalid user input, ensuring robustness.
'''

def calculate_total_bill():
    # Prompt the user to enter the quantity of coffee cups
    try:
        quantity = int(input("Enter the number of coffee cups: "))
        if quantity < 0:
            raise ValueError("The quantity cannot be negative.")

        # Prompt the user to enter the price per coffee cup
        price_per_cup = float(input("Enter the price per coffee cup: "))
        if price_per_cup < 0:
            raise ValueError("The price cannot be negative.")

        # Calculate the total bill amount
        total_bill = quantity * price_per_cup

        # Display the total bill amount
        print(f"The total bill amount is: R{total_bill:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")

# Execute the function
calculate_total_bill()

print("Hello! I'm a simple math chatbot.")
print("I can perform basic mathematical operations with two operands.")
print("Let's get started!")

# Greet the user
print("Hi there! How can I assist you with math today?")

# Keep executing until the user decides to stop
while True:
    # Ask the user what they want to do
    action = input("What do you want to do? You can ask me a math question or type 'stop' to exit: ")
    
    # Check if the user wants to stop
    if action.lower() == 'stop':
        break
    
    # Get the first operand
    while True:
        try:
            operand1 = float(input("Please enter the first operand: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get the operator
    while True:
        operator = input("Please enter the operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid operator. Please enter +, -, *, or /.")

    # Get the second operand
    while True:
        try:
            operand2 = float(input("Please enter the second operand: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Perform the mathematical operation
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            print("Error: division by zero")
            result = None
        else:
            result = operand1 / operand2
    else:
        print("Error: unrecognized operator")
        result = None

    # Display the result or prompt the user to stop
    if result is not None:
        print("The result is:", result)
    else:
        print("Sorry, I could not perform the requested operation.")

# Say goodbye to the user
print("Thank you for using this math chatbot. Goodbye!")

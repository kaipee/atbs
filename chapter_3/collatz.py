# THE COLLATZ SQUEEZE

def collatz(number):                      # Function named collatz that has one paramter named "number"
    if (number % 2) == 0:                 # Check if number is even
        result = (number // 2)            # If even, get the result of (number // 2)
        print(result)                     # Print the result
        return result                     # Return the result
    elif (number % 2) == 1:               # Check if number is odd
        result = (3 * number + 1)         # If odd, get the result of (3 * number + 1)
        print(result)                     # Print the result
        return result                     # Return the result

def getValue():                           # Define function for obtaining user input
    global i                              # Call global function i
    i = input('Please input a number : ') # Get input from user and assign to global variable

getValue()                                # Call function to obtain user unput
while i != 1:                             # Execute function while input value is not 1
    try:                                  # Handle integers
        i = collatz(int(i))               # Assign i to return value of collatz and execute collatz function on i
    except ValueError:                    # Handle non-integers
        print('Error: Not a NUMBER!')     # Notify user of non-integer
        print()
        getValue()                        # Re-call function to create sense of continuing program

# This program says hello and asks for your name

print('Hello world!')   # Print a greeting to the screen
print('What is your name?')   # Ask for the user's name
myName = input()    # Obtain the user's name from input and assign to variable myName
print('It is good to meet you, ' + myName)  # Print a greeting back to the user
print('The length of your name is:')    
print(len(myName))  # Calculate and display the string length of the supplied name

print('What is your age?')  # Ask for user's age
myAge = input()     # Obtain the user's age from input and assign to variable myAge
print('You will be ' + str(int(myAge) + 1) + ' in a year.')     # Calculate and output the age of the user after 1 year

# Summer Times Project - Conditional Statements

# Introduction
print("Welcome to Rohan's Weather Program!")
print("Let's help Rohan decide if he can wear light clothes today.\n")

# Input: Get temperature from the user
temperature = int(input("Enter today's temperature in degrees Celsius: "))

# Conditional statements to check the weather and give advice
if temperature >= 25:
    print("It's warm enough! Rohan can wear light clothes.")
elif 15 <= temperature < 25:
    print("It's a bit cool. Rohan can wear light clothes but also carry a jacket.")
else:
    print("It's too cold! Rohan should wear warm clothes like a jacket or pullover.")

# Thank you message
print("\nThanks for helping Rohan stay comfortable today!")

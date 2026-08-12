list_of_digits= [0,1,2,3,4,5]
guessing_digit= int(input("Guess a digit: "))
for digit in list_of_digits:
    if digit == guessing_digit:
        print("You guessed it right!")
        break
else:
    print("Sorry, that's not the correct digit.")


secret_word = "hummer"
userword = ""
guess_no = 1
guess_limit = 4
out_of_guesses = False

while userword != secret_word and not (out_of_guesses):
    if guess_no <= guess_limit:
        userword = input("Enter your guess: ")
        guess_no += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry you loser, ran out of guesses!")
else:
    print("You won!")

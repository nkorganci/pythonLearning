# 1
i = 0
while i < 10:
    print(i)
    i += 1

# 2 secret word - guess
secret_word = "secret"
guess = ""
guess_count = 1
out_of_guess = False

while guess != secret_word:
    if guess_count <= 3:
        guess = input("Enter the secret word: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("Looser :)")
else:
    print("Winner")

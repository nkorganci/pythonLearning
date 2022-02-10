# 1
i = 0
while i < 10:
    print(i)
    i += 1

# 2 secret word - guess with limited try, write if you are looser or winner

count = 1
max_count = 4
secret_word = "Harmony"
guessed = False

while count < max_count and not guessed:
    guess = input("Guess the secret word: ")
    if secret_word == guess:
        guessed = True
    count += 1

if guessed:
    print("Winner")
else:
    print("Looser")
print("While loop has finished")

import random

low = 1
high = 1000
max_num_guesses = 10
random_secret = True
show_secret = True
human_player = False

if random_secret:
    # the computer sets the secret
    secret = random.randint(low, high)
else:
    # otherwise player chooses secret
    secret = int(input("Please input the secret (1-1000): "))
    assert secret <= 1000 and secret >= 1
if show_secret:
    print('secret', secret)

for guess_count in range(0, max_num_guesses):
    print(guess_count, 'guesses so far')
    if human_player:
        guess = int(input("Please input your next guess: "))
    else:
        # split in the middle
        guess = (low + high) // 2

    guess_count += 1
    if guess > secret:
        print('too high')
        high = guess - 1
    elif guess < secret:
        print('too low')
        low = guess + 1
    else: # guess == secret
        print('You guessed right!')
        break
else:
    print('Too many guesses... the answer was', secret)


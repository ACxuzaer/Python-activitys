secret = 27
attempts = 5
used = 0
won = False

print("Guess the number between 1 and 50. You have 5 attempts!")

while used < attempts and not won:
    guess = int(input("Enter your guess: "))
    used += 1

    if guess == secret:
        won = True
    else:
        diff = abs(secret - guess)

        if diff > 20:
            print("🧊 Ice cold")
        elif diff > 10:
            print("🥶 Cold")
        elif diff > 5:
            print("🌡️ Warm")
        else:
            print("🔥 Hot")

        remaining = attempts - used
        for i in range(remaining):
            print("❤️", end=" ")
        print(f" ({remaining} remaining)")

if won:
    print(f"🎉 You win! The number was {secret}.")
else:
    print(f"💀 You lose! The secret number was {secret}.")
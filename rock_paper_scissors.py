import random

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type your choice: rock, paper, or scissors")

user_score = 0
computer_score = 0
rounds = 3

options = ["rock", "paper", "scissors"]

for round in range(1, rounds + 1):
    print(f"\n🔁 Round {round}")
    user_choice = input("Your choice: ").lower()

    if user_choice not in options:
        print("❌ Invalid choice. You lose this round.")
        computer_score += 1
        continue

    computer_choice = random.choice(options)
    print(f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("⚖️ It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round.")
        computer_score += 1

print("\n🏁 Final Score:")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("🎉 You win the game!")
elif computer_score > user_score:
    print("😢 Computer wins the game.")
else:
    print("🤝 It's a tie game!")

print("\nThanks for playing, Somesh! 👋")

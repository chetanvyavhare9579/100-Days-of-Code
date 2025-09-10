import random
import time

def print_rules():
    print("\n📜 Rules of Rock-Paper-Scissors:")
    print("✊ Rock beats ✌️ Scissors")
    print("✋ Paper beats ✊ Rock")
    print("✌️ Scissors beats ✋ Paper")
    print("First to win 3 rounds out of 5 is the Champion! 🏆")
    print("-" * 50)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "player"
    else:
        return "computer"

def rock_paper_scissors():
    print("🎮 Welcome to the Ultimate Rock-Paper-Scissors Game!")
    print_rules()

    while True:
        player_score = 0
        computer_score = 0
        rounds = 0

        while player_score < 3 and computer_score < 3 and rounds < 5:
            print(f"\nRound {rounds + 1} of 5")
            print(f"Score: You {player_score} - {computer_score} Computer")

            player = input("👉 Enter rock/paper/scissors: ").lower()

            if player not in ["rock", "paper", "scissors"]:
                print("⚠️ Invalid input! Please type rock, paper, or scissors.")
                continue

            computer = get_computer_choice()
            print("🤔 Computer is choosing...")
            time.sleep(1)  # dramatic pause
            print(f"💻 Computer chose: {computer}")

            result = decide_winner(player, computer)

            if result == "tie":
                print("🤝 It's a tie!")
            elif result == "player":
                player_score += 1
                print("🎉 You win this round!")
            else:
                computer_score += 1
                print("😢 Computer wins this round!")

            rounds += 1
            print("-" * 30)

        # Final result
        print("\n🏆 Final Score:")
        print(f"You {player_score} - {computer_score} Computer")

        if player_score > computer_score:
            print("🎊 Congratulations! You are the Champion!")
        elif computer_score > player_score:
            print("🤖 Computer is the Champion! Better luck next time.")
        else:
            print("🤝 It's an overall Tie!")

        # Replay option
        again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    rock_paper_scissors()


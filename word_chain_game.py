import random

# Load the dictionary of valid words
def load_words(file_path):
    try:
        with open(file_path, "r") as file:
            words = set(word.strip().lower() for word in file if word.strip().isalpha())
        return words
    except FileNotFoundError:
        print("❌ Error: 'words.txt' file not found in project folder!")
        exit()

# Get a list of words starting with a specific letter
def words_starting_with(words_set, letter):
    return [word for word in words_set if word.startswith(letter)]

# Main game logic
def play_game():
    words = load_words("words.txt")
    used_words = set()

    print("\n🎮 Welcome to the Word Chain Game!")
    print("📌 Rule: Each word must start with the last letter of the previous word.")
    print("❗ Type 'exit' anytime to quit.\n")

    # Get player's first word
    user_word = input("👉 Enter your first word: ").strip().lower()

    if user_word == "exit":
        print("👋 Exiting game. Goodbye!")
        return

    if user_word not in words:
        print("❌ Word not in dictionary!")
        return

    used_words.add(user_word)
    current_letter = user_word[-1]

    while True:
        # AI turn
        ai_options = [w for w in words_starting_with(words, current_letter) if w not in used_words]
        if not ai_options:
            print("✅ You win! No more words left for AI.")
            break

        ai_word = random.choice(ai_options)
        print(f"🤖 AI's turn: {ai_word}")
        used_words.add(ai_word)
        current_letter = ai_word[-1]

        # User turn
        user_word = input(f"👉 Your word (start with '{current_letter}'): ").strip().lower()

        if user_word == "exit":
            print("👋 Game ended. Thanks for playing!")
            break

        if user_word in used_words:
            print("❌ You've already used that word!")
            break

        if not user_word.startswith(current_letter):
            print(f"❌ Invalid! Word must start with '{current_letter}'.")
            break

        if user_word not in words:
            print("❌ Word not in dictionary!")
            break

        used_words.add(user_word)
        current_letter = user_word[-1]

# Run the game
if __name__ == "__main__":
    play_game()

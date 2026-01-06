def analyze_text(text):
    words = text.split() 
    word_count = len(words)

    char_count_total = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))

    sentence_count = text.count('.') + text.count('!') + text.count('?')

    print("\n--- TEXT ANALYSIS RESULTS ---")
    print(f"Total Words: {word_count}")
    print(f"Total Characters (with spaces): {char_count_total}")
    print(f"Total Characters (no spaces): {char_count_no_spaces}")
    print(f"Approximate Sentences: {sentence_count}")
    print("-----------------------------")

if __name__ == "__main__":
    print("Welcome to the Text Analyzer!")
    user_input = input("Please paste your text here:\n")
    
    if len(user_input.strip()) == 0:
        print("You didn't enter any text!")
    else:
        analyze_text(user_input)

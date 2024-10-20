def main():
    # Count Occurrences of Words in String

    text = input("Text: ")
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1  # Increment count if word already exists
        else:
            word_counts[word] = 1   # Initialize count if word is new

    # Display words and their frequencies
    for word, count in word_counts.items():
        print(f"{word} : {count}")  # Print word and its count

if __name__ == "__main__":
    main()
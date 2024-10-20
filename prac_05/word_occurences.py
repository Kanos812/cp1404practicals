def main():
    # Count Occurrences of Words in String

    text = input("Text: ")
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find the longest word for formatting
    max_word_length = 0
    for word in word_counts:
        if len(word) > max_word_length:
            max_word_length = len(word)

    # Display words and their frequencies, sorted and aligned
    for word in sorted(word_counts):
        print(f"{word:{max_word_length}} : {word_counts[word]}")

if __name__ == "__main__":
    main()


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

    # Display words with associated no of characters
    for word in word_counts:
        print(f"{word} : {len(word)}")

if __name__ == "__main__":
    main()
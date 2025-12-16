def count_words(filename):
    word_count = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.lower()
            for ch in ".,!?;:\"()[]{}":
                line = line.replace(ch, "")
            for word in line.split():
                word_count[word] = word_count.get(word, 0) + 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words:
        print(word, count)


# CALL THE FUNCTION
count_words(r"C:\Users\stati\Downloads\sample2.txt")

def CounterOfWords(text):
    words = text.split()
    dictionary = {}

    for word in words:
        word = word.lower()  
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary


def main():
    text = input("Podaj tekst: ")

    word_counts = CounterOfWords(text)

    print("\nLiczba wystąpień słów:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    print("\n3 najczęstsze słowa:")
    top3 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    for word, count in top3:
        print(f"{word}: {count}")


if __name__ == '__main__':
    main()

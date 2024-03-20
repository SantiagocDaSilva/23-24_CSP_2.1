def two_words(password):
    words = get_dictionary()
    guesses = 0
    for w in words:
        for w2 in words:
            guesses += 1
            if w + w2 == password:
                return True, guesses
        return False, guesses
def get_counts(wordlist):
    count = [0] * 10
    for word in wordlist:
        if len(word) < 10:
            count[len(word)] += 1

    return count
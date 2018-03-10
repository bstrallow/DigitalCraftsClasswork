def letterHistogram(word):
    tally = {}
    for letter in word:
        if tally.get(letter):
            tally[letter] += 1
        else:
            tally[letter] = 1
    print tally

letterHistogram('banana')

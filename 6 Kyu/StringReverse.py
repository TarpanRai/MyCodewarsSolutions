# Given a string, if the word length is 5 or longer,
# reverse that word


def spin_words(sentence):
    split_sen = sentence.split()
    for i in range(0, len(split_sen)):
        if len(split_sen[i]) >= 5:
            split_sen[i] = split_sen[i][::-1]
            i += 1
        else:
            i += 1
    split_sen = ' '.join(split_sen)
    return split_sen

# Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).
# Output: The number of words in the text as an integer.
# count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
# count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2


def count_words(text, words):
    text = text.lower()
    res = 0
    for i in words:
        if text.count(i) > 0:
            res += 1
    return res


if __name__ == '__main__':
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

# print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))

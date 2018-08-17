# Here you should find the length of the longest substring that consists of the same letter.
# For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
# The last substring is the longest one which makes it an answer.


def long_repeat(line):
    res = 1
    tmp = 1
    i = 0
    while i < len(line):
        if i < len(line) - 1 and line[i] == line[i + 1]:
            tmp += 1
            # print(tmp, line[i])
        else:
            if tmp > 1:
                if tmp > res:
                    res = tmp
                tmp = 1
        i += 1
    if len(line) > 0:
        return res
    return 0


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

# print("RESULT is: ", long_repeat("ddvvrwwwrggg"))

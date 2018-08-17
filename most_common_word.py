
def checkio(txt):
    txt = txt.lower()
    dict = {}
    # len = 0
    for i in range(len(txt)):
        tmp = 1
        for k in range(i + 1, len(txt)):
            # print(txt[k])
            if txt[i].isalpha() and txt[i] == txt[k] and txt[i] not in dict:
                tmp += 1
        if txt[i].isalpha() and txt[i] not in dict:
            dict[txt[i]] = tmp
    # print(res)
    tmp = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print(tmp)
    if len(tmp) > 1 and tmp[0][1] == tmp[1][1]:
        print("IN KELPER")
        return helper(tmp)
    print("HAVE A RES")
    return tmp[0][0]


def helper(data):
    print(data)
    tmp = []
    print(len(data))
    for i in range(len(data) - 1):
        if data[i][1] == data[i + 1][1]:
            tmp.append(data[i])
            if i == len(data) - 2 or data[i + 1][1] > data[i + 2][1]:
                tmp.append(data[i + 1])
                break
    # print(tmp)
    tmp = sorted(tmp)
    return tmp[0][0]


# if __name__ == '__main__':
#     print("Example:")
#     print(checkio("Hello World!"))
#     assert checkio("Hello World!") == "l", "Hello test"
#     assert checkio("How do you do?") == "o", "O is most wanted"
#     assert checkio("One") == "e", "All letter only once."
#     assert checkio("Oops!") == "o", "Don't forget about lower case."
#     assert checkio("AAaooo!!!!") == "a", "Only letters."
#     assert checkio("abe") == "a", "The First."
#     assert checkio("Lorem ipsum dolor sit amet") == "m", "YAKOGO HUYA?"
#     print("Start the long test")
#     print("The local tests are done.")

# print(checkio("Aaaaaaaaaaaaaaaa!!!!"))
print(str)
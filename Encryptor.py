def to_encrypt(text, delta):
    min = ord("a")
    max = ord("z")
    res = ""
    for i in text:
        if i.isalpha():
            if ord(i) + delta > max:
                tmp = (ord(i) + delta - max) + min - 1
            elif ord(i) + delta < min:
                tmp = (ord(i) + delta - min) + max + 1
            else:
                tmp = ord(i) + delta
            res += chr(tmp)
        else:
            res += i
    return res


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")


# print(to_encrypt("simple text", 16))
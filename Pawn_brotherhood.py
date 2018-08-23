def safe_pawns(pawns: set) -> int:
    ps = set()
    res = 0
    for i in pawns:
        row = int(i[1]) - 1
        col = ord(i[0]) - 97
        ps.add((col, row))
    for l, d in ps:
        is_safe = ((l - 1, d - 1) in ps) or ((l + 1, d - 1) in ps)
        if is_safe:
            res += 1
    return res


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# print(safe_pawns({"a4", "d4", "f4", "c3", "e3", "g5", "d2"}))









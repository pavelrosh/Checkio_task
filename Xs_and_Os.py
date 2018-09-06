# Input: A game result as a list of strings (unicode).
#
# Output: "X", "O" or "D" as a string.

from typing import List


def create_list(game_result):
    check_list = []
    k = 0
    while k < 3:
        check_list.append(game_result[k])
        n = 0
        tmp = ""
        while n < 3:
            tmp += game_result[n][k]
            n += 1
        check_list.append(tmp)
        k += 1
    k = 0
    tmp = ""
    while k < 3:
        tmp += game_result[k][k]
        k += 1
    check_list.append(tmp)
    k = 0
    n = 2
    tmp = ""
    while n >= 0:
        tmp += game_result[k][n]
        k += 1
        n -= 1
    check_list.append(tmp)
    return check_list


def checkio(game_result: List[str]) -> str:
    check = create_list(game_result)
    for i in check:
        if "XXX" in i:
            return "X"
        elif "OOO" in i:
            return "O"
    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# print (checkio(["XXX",
#          "X.X",
#          "OOX"]))
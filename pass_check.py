def checkio(str):
    s = 0
    b = 0
    num = 0
    if len(str) >= 10 and str.isalnum():
        for i in str:
            if i >= chr(65) and i <= chr(90):
                b += 1
            elif i >= chr(97) and i <= chr(122):
                s += 1
            elif i >= chr(48) and i <= chr(57):
                num += 1
        if b > 0 and s > 0 and num > 0:
            return True
    return False


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

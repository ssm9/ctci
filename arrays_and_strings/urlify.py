def urlify(s: str, l: int) -> str:
    """
    Given a string with spaces, and the correct length of the string, replace all ' ' with "%20"
    This is done by moving backwards through the string
    :param s: the string to modify
    :param l: the true length of the string
    :return: the modified string
    """
    s = list(s)
    i = len(s) - 1
    while(i > -1):
        if s[l - 1] is ' ':
            s[i] = '0'
            i -= 1
            s[i] = '2'
            i -= 1
            s[i] = '%'
        else:
            s[i] = s[l - 1]
        l -= 1
        i -= 1
    return ''.join(s)


if __name__ == '__main__':
    print(urlify("Mr John Smith    ", 13))

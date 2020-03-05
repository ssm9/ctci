def palindrome_permutation(s: str) -> bool:
    """
    Checks if a given string is a permutation of some palindrome
    Uses a dictionary to count the number of occurrences for all characters in the string
    A palindrome is only a palindrome if every character appears an even number of times
    Except maybe for one character in the middle
    :param s: the string to check
    :return: True if the string is a permutation of a palindrome, False otherwise
    """
    s_chars = {}
    for c in s:
        if not c.isspace():
            count_c = s_chars.get(c, 0)
            count_c += 1
            s_chars.update({c: count_c})
    # there can only be one character that shows up an odd number of times
    num_odds = 0
    for v in s_chars.values():
        num_odds += 1 if v & 1 else 0
        if num_odds > 1:
            return False
    return True

if __name__ == '__main__':
    print(palindrome_permutation("tact coa"))
    print(palindrome_permutation("tact cot"))
    print(palindrome_permutation("tttt ccc"))
    print(palindrome_permutation("racecar"))
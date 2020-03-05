def check_permutation(s1: str, s2: str) -> bool:
    """
    Checks if two strings are permutations of each other by using dictionaries for each
    Then it checks each entry of one of the dictionaries agains the entries of the other
    Permutations would have the same characters the same number of times in both strings
    :param s1: one of the strings to check
    :param s2: the other string to check
    :return: True if the strings are permutations, False otherwise
    """
    s1_chars = {}
    s2_chars = {}
    for c in s1:
        count_c = s1_chars.get(c, 0)
        count_c += 1
        s1_chars.update({c: count_c})
    for c in s2:
        count_c = s2_chars.get(c, 0)
        count_c += 1
        s2_chars.update({c: count_c})
    for k, v in s1_chars.items():
        if s2_chars.get(k, 0) != v:
            return False
    return True

if __name__ == '__main__':
    print(check_permutation("sai", "ias"))
    print(check_permutation("sai", "sss"))
    print(check_permutation("asdfasdf", "fdsa"))
    print(check_permutation("asdf", ""))
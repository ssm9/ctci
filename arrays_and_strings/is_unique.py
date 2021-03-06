def is_unique(s: str) -> bool:
    """
    Checks if a string contains all-unique characters by using a bit_vector
    If a bit in the vector is set to 1, then that character has already been seen - immediately return false
    :param s: the string to check
    :return: True if the string has unique characters only, False otherwise
    """
    bit_vector = 0
    for c in s:
        if bit_vector & (1 << (ord(c) - ord('a'))):
            return False
        bit_vector = bit_vector | (1 << (ord(c) - ord('a')))
    return True


if __name__ == '__main__':
    assert is_unique("") is True
    assert is_unique("abcde") is True
    assert is_unique("abcda") is False

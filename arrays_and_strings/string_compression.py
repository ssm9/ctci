def string_compression(s: str) -> str:
    """
    Compresses a string using the count of each letter
    A counter is maintained for each character that is different from the previous character
    If, at any time, the length of the new string is as long as the original string, the original string is returned
    :param s: the string to compress
    :return:
    """
    c_count = 0
    prev_c = s[0]
    new_length = 0
    compressed = ""
    for c in s:
        if c is prev_c:
            c_count += 1
        else:
            compressed += f"""{prev_c}{c_count}"""
            new_length += len(f"""{prev_c}{c_count}""")
            if new_length >= len(s):
                return s
            prev_c = c
            c_count = 1
    compressed += f"""{prev_c}{c_count}"""
    new_length += len(f"""{prev_c}{c_count}""")
    if new_length >= len(s):
        return s
    return compressed


if __name__ == '__main__':
    string_compression('aabcccccaaa')

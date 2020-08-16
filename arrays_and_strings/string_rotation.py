def string_rotation(s1: str, s2: str):
    concat = s2 + s2
    return s1 in concat

if __name__ == '__main__':
    print(string_rotation("waterbottle", "erbottlewat"))

def one_away(s1: str, s2: str) -> bool:
    # if the size difference is more than one, then you cannot insert OR delete just 1 character to get the other string
    if abs(len(s1) - len(s2)) > 1:
        return False

    return True
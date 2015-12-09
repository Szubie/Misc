# Return the Levenshtein distance between two strings
def approxMatch(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if (len1 == 0):
        return len2
    if (len2 == 0):
        return len1

    match = approxMatch(str1[1:len1], str2[1:len2])
    if (str1[0] != str2[0]):
        match = match + 1

    del1 = 1 + approxMatch(str1[1:len1], str2)
    del2 = 1 + approxMatch(str1, str2[1:len2])

    return min(match, del1, del2)

print approxMatch("ATGGA", "ATCGGA")

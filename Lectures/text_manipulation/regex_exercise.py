def main():
    # match specific character strings
    test = "abc abcdef defabc"
    rep = r"abc"
    findall(rep, test)
    rep = r"\w*abc\w*"
    findall(rep, test)

    test = "abc adc afc"
    rep = r"a[bdf]c"
    findall(rep, test)

    numtest = "123 123abc abc123abc"
    rep = r"123"
    findall(rep, numtest)
    rep = r"\d\d\d"
    findall(rep, numtest)
    rep = r"\w*\d\d\d\w*"
    findall(rep, numtest)
    
    test = "abcdefghi abc123ghi abcXXXghi"
    rep = r"abc...ghi"
    findall(rep, test)


def findall(regex_pattern, test):
    import re
    print("Original String: %s" % test)
    print("RegEx Pattern: %s" % regex_pattern)
    m = re.findall(regex_pattern, test)
    input("Press a key to advance...")
    print("Found Matches: %s\n" % m)


if __name__ == "__main__":
    main()

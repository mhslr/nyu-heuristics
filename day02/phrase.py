# PHRASE ANALYSIS

phrase = input("PLEASE INPUT PHRASE: ")
print("LEN: " + str(len(phrase)))
print("FIRST LETTER: " + phrase[0])
print("LAST LETTER: " + phrase[-1])
print("MIDDLE LETTER: " + phrase[int(len(phrase) // 2)])
print("BACKWARDS: " + phrase[::-1])
print("UPPERCASE: " + phrase.upper())
print("LOWERCASE: " + phrase.lower())
print("TITLE: " + phrase.title())
print((phrase.split("e")))
print("NUMBER OF WORDS: " + str(len(phrase.split(" "))))


def analyzePhrase(myphrase):
    print("In analyzePhrase....")
    print("LEN: " + str(len(myphrase)))
    print("FIRST LETTER: " + myphrase[0])
    print("LAST LETTER: " + myphrase[-1])
    print("MIDDLE LETTER: " + phrase[int(len(phrase) // 2)])
    print("BACKWARDS: " + myphrase[::-1])
    print("UPPERCASE: " + myphrase.upper())
    print("LOWERCASE: " + myphrase.lower())
    print("TITLE: " + myphrase.title())
    print("NUMBER OF WORDS: " + str(len(myphrase.split(" "))))


analyzePhrase(phrase)

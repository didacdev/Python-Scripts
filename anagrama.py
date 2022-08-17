""" It compares two words and returns true or false depending on whether they are an anagram or not """


def esAnagrama(word1: str, word2: str):
    """ 
        It compares the two words

        Parameters:
        word1 (str): first word
        word2 (str): second word

        Returns:
        boolean: true if the words are an anagram or false if they aren't

    """
    anagrama = True

    if word1 == word2:
        anagrama = False

    else:

        word1 = sorted(word1)
        word2 = sorted(word2)

        if word1 != word2:
            anagrama = False

    return anagrama


word1 = input("> ")  # gets the word1
word2 = input("> ")  # gets the word2

print(esAnagrama(word1, word2))

"""
Create a class named StringManipulation that has the following specification:

Attributes
words: list of strings, all of which will be in lower case

Methods
    (1) __init__: accept a list words as argument and assign it to the
corresponding attribute
    (2) total_words: return the total number of words in words
    (3) count: accept an argument named some_word and return the number of
    times this word occurs in the list words
    (4) words_of_length: accept a positive integer length as argument and
    return a list of all the words in the list words that have a length equal
    to length
    (5) words_start_with: accept a character char as argument and return the
    list of all the words in words that start with char
    (6) longest_word: return the longest word in the list words; if there are
multiple words that satisfy this condition, return the first such occurrence
    (7) palindromes: return a list of all the words that are palindromes in
    words
"""


class StringManipulation():

    def __init__(self, words):
        self.words = words

    def total_words(self):
        total_words = len(self.words)
        return total_words

    def count(self, some_word):
        count = 0
        for i in self.words:
            if i == some_word:
                count += 1

        return count

    def words_of_length(self, length):
        words_list = []
        for i in self.words:
            if len(i) == length:
                words_list.append(i)

        return words_list

    def words_start_with(self, char):
        words_list = []
        for i in self.words:
            if i[0] == char:
                words_list.append(i)

        return words_list

    def longest_word(self):
        longest_word = self.words[0]
        for i in self.words:
            if len(i) > len(longest_word):
                longest_word = i

        return longest_word

    def palindromes(self):
        palindromes = []
        for i in self.words:
            if i == i[::-1]:
                palindromes.append(i)

        return palindromes

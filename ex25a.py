def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted (words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

stuff_words = """
One ring to rule them all,
one ring to find them.
One ring to bring them all,
and in the darkness bind them."""

broken_words = break_words(stuff_words)

print("\n#1 var broken_words:", broken_words)

print("\n#2 function break_words(stuff_words):", break_words(stuff_words))

print("\n#3 does var broken_words == function break_words(stuff_words)?\t", broken_words == break_words(stuff_words))

print("\n#4 sort_words(broken_words):", sort_words(broken_words))

print("\n#5 sort_words(stuff_words):", sort_words(stuff_words))

print("\n#6 sort_words(broken_words) == sort_words(stuff_words)", sort_words(broken_words) == sort_words(stuff_words))

print("\n#7 print_first_word(broken_words):", print_first_word(broken_words))

print("\n#8 print_last_word(broken_words):", print_last_word(broken_words))

print("\n#9 sort_sentence")

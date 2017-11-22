# This line creates the function 'break_words' and
# give it space for one argument called 'stuff'.
# ISSUES WITH THE FUNCTION = None that I can see.
def break_words(stuff):
    """This function will break up words for us."""
    # This line creates the var 'words' and assigns
    # it the value of the argument 'stuff' with the
    # contents of 'stuff' being split up with the
    # spaces between words being used as the markers
    # for where to make the split. Empty space is
    # filled with a comma and the substrings before
    # and after the comma are put inbetween single
    # quotes. I think this is the first time i've
    # seen the split command. I found it confusing
    # at first but it's starting to make sense.
    words = stuff.split(' ')
    # This line returns the value of var 'words'
    return words

# This line creates the function 'sort_words' and
# gives it space for one argument called 'words'.
# ISSUES WITH THE FUNCTION = None that I can see.
def sort_words(words):
    """Sorts the words."""
    # This line breaks the value of the words argument
    # into its commponent parts and then sorts them
    # into either numerical or alphabetical order. It
    # then returns that value to the computers memmory
    # as the assigned value of the 'sort_words'
    # function.
    return sorted(words)

# This line creates a function called
# 'print_first_word' and gives it space for one
# arg called 'words'.
# ISSUES WITH THE FUNCTION = I think it would be better
# to 'return' the value of var 'word' instead of 'print'
# them.
def print_first_word(words):
    """Prints the first word after popping it off."""
    # This line creates a var within the function
    # called 'word', which is given the value of the
    # first item in a list object that is being passed
    # into the 'words' arg.
    # Note: the 'pop' command only works on list objects.
    # to use it on an iterable you must first pass the
    # iterable through the 'split' command and then
    # assigne the returned value from that opperation to
    # a var. You then pass THAT var into this function.
    word = words.pop(0)
    # This line prints the value of var 'word'.
    print(word)

# This line creates a function named
# 'print_last_word' and gives it space for one
# arg tittled 'words'.
# ISSUES WITH THE FUNCTION = Once again I think it is
# supperior to return the value of the 'word' arg instead
# of print it.
def print_last_word(words):
    """Prints the last word after popping it off."""
    # This line creates a var, withing the function
    # called 'word' and assgns it the value of the
    # last item in the list object that has been
    # passed into arg 'words', and 'popped' off of
    # that list item.
    word = words.pop(-1)
    # prints the value of var 'word'.
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# ---------
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

# OVERARCHING ERRORS =
#1 First and foremost is that none of these functions
# have actually been called.

#2 There is no text file or var with a string value
# to pass through the functions as an argument.

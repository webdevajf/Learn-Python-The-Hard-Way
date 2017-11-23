# This line creates the function 'break_words' and
# give it space for one argument called 'stuff'.
# ISSUES WITH THE FUNCTION = None that I can see.
def break_words(stuff):
    # This line creates a lie of text that will appear
    # in the terminal if we querry python for 'help()'
    # (from within the terminal) and place the name
    # of the file + . + the name of this function
    # (ie: 'help(ex25.break_words)') within the help
    # brackets.
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
# ISSUES WITH THE FUNCTION = If you feed a string
# directly into this function it will break it up
# into its smallest commponents i.e. individual
# string characters. If you want it to break the
# string into individual words there are two ways
# to do it. #1 feed the string, as a arg, into a var
# that runs it through the .split() command and then
# pass that var as the arg in this function. #2 You
# can attach the .split() command to the 'words' arg
# in this function and pass the var with the string
# value into this funcion as its arg.
def sort_words(words):
    # This line creates a lie of text that will appear
    # in the terminal if we querry python for 'help()'
    # (from within the terminal) and place the name
    # of the file + . + the name of this function
    # (ie: 'help(ex25.sort_words)') within the help
    # brackets.
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
# ISSUES WITH THE FUNCTION =
#1 I think it is supperior to return the value of the
# 'word' arg instead of print it.
#2 When I called this function, in a print statement,
# I placed a str before the function call which explaines
# what the printed data is. Someting about the 'pop'
# command causes the 'popped' word to appear before the
# print statement. It's very confusing, it doesn't look
# right to me, and I can figure out why it's doing this.
def print_first_word(words):
    # This line creates a lie of text that will appear
    # in the terminal if we querry python for 'help()'
    # (from within the terminal) and place the name
    # of the file + . + the name of this function
    # (ie: 'help(ex25.print_first_word)') within the
    # help brackets.
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
# ISSUES WITH THE FUNCTION =
#1 I think it is supperior to return the value of the
# 'word' arg instead of print it.
#2 When I called this function, in a print statement,
# I placed a str before the function call which explaines
# what the printed data is. Someting about the 'pop'
# command causes the 'popped' word to appear before the
# print statement. It's very confusing, it doesn't look
# right to me, and I can figure out why it's doing this.
def print_last_word(words):
    # This line creates a lie of text that will appear
    # in the terminal if we querry python for 'help()'
    # (from within the terminal) and place the name
    # of the file + . + the name of this function
    # (ie: 'help(ex25.print_last_word)') within the
    # help brackets.
    """Prints the last word after popping it off."""
    # This line creates a var, withing the function
    # called 'word' and assgns it the value of the
    # last item in the list object that has been
    # passed into arg 'words', and 'popped' off of
    # that list item.
    word = words.pop(-1)
    # prints the value of var 'word'.
    print(word)

# This line creates a function named 'sort_sentence' and
# and gives it space for one arg titled 'sentence'.
# ISSUES WITH THE FUNCTION = It doesn't break the string
# object, that is passed into it, into componnent
# sentences. I don't yet know how to do that.
def sort_sentence(sentence):
    # This line creates a lie of text that will appear
    # in the terminal if we querry python for 'help()'
    # (from within the terminal) and place the name
    # of the file + . + the name of this function
    # (ie: 'help(ex25.sort_sentence)') within the help
    # brackets.
    """Takes in a full sentence and returns the sorted words."""
    # This line creates the var 'words' and assigns
    # it the value of function break_words' with the
    # arg 'sentence' passed into it.
    words = break_words(sentence)
    # This line returns the value of function
    # 'sort_words' with the value of var 'words'
    # passed into it.
    return sort_words(words)

# This line creates the funtion 'print_first_and_last'
# and give it space for one arg named 'sentence'.
# ISSUES WITH THE FUNCTION =
#1 When I called this function, in a print statement,
# I placed a str before the function call which explaines
# what the printed data is. Someting about the 'pop'
# command causes the 'popped' words to appear before the
# print statement. It's very confusing, it doesn't look
# right to me, and I can figure out why it's doing this.
def print_first_and_last(sentence):
    # This line creates a lie of text that will appear
    # in the terminal if we querry python for 'help()'
    # (from within the terminal) and place the name
    # of the file + . + the name of this function
    # (ie: 'help(ex25.print_first_and_last)') within
    # the help brackets.
    """Prints the first and last words of the sentence."""
    # This line creates var 'words' and assigns it
    # the value of function 'break_words' with arg
    # 'sentence' passed into it.
    words = break_words(sentence)
    # This line calls the function 'print_first_word'
    # and passes the var 'words' into it as an arg.
    print_first_word(words)
    # This line calls the function 'print_last_word'
    # and passes the var 'words' into it as an arg.
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    # This line creates a lie of text that will appear
    # in the terminal if we querry python for 'help()'
    # (from within the terminal) and place the name
    # of the file + . + the name of this function
    # (ie: 'help(ex25.print_first_and_last_sorted)')
    # within the help brackets.
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# OVERARCHING ERRORS =
#1 First and foremost is that none of these functions
# have actually been called.

#2 There is no text file or var with a string value
# to pass through the functions as an argument.

# note --> The above 'OVERARCHING ERRORS' are wrong!
# I did not read ahed in the exerecise and so did not
# understand that these functions will be called from
# within the terminal, which in this format they are
# fully equiped to do if the args to be put into them
# are defigned from withn the terminal.

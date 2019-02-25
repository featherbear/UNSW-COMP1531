

def count_char(text):
    # TODO count the number of times each character occurs in the text
    # and print out each character along with its count
    [print(f'{c} {text.count(c)}') for c in sorted(set(text), key=text.index)]

def count_char_insensitive(text):
    # TODO do the same as `count_char` but in a case-insensitive manner
    count_char(text.lower()) # But by case-insensitive they actually just mean lowercase smh

def count_char_ordered(text):
    # TODO print the characters in the descending order of the count
    # HINT: lookup `sorted()` in the Python documentation
    
    # This task is quite difficult, so please feel free to make use of
    # resources online (Python docs, Stack Overflow, etc.)
    
    [print(f'{pair[0]} {pair[1]}') for pair in sorted(zip(set(text.lower()), map(lambda c: text.lower().count(c), set(text.lower()))), key = lambda c: (c[1], len(text) - text.lower().index(c[0])), reverse = True)]
def add_string(word):

    if len(word) < 3:
        return word
    elif word[-3:] == 'ing':
        return word + 'ly'
    else:
        return word + 'ing'


   

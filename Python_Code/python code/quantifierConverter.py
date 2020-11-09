# Write a function called quantifierConverter that takes a string as input and
# returns a string where every instance of the phrase "for every" is replaced
# with the symbol for it and every instance of the phrase "there exists"
# is replaced with the symbol for it. Ignore punctuation and capitalization.

def quantifierConverter(input_string):
    input_string = input_string.split(' ')

    universal_str = 'for every'
    existential_str = 'there exists'
    universal_char = '\u2200'
    existential_char = '\u2203'

    return_string = ''
    i=0
    while i<len(input_string):

        if input_string[i]=='for' and input_string[i+1]=='every':
            return_string+=universal_char
            i+=2

        elif input_string[i]=='there' and input_string[i+1]=='exists':
            return_string+=existential_char
            i+=2

        elif input_string[i]==universal_char:
            return_string+=universal_str
            i+=1

        elif input_string[i]==existential_char:
            return_string+=existential_str
            i+=1

        else:
            return_string+=input_string[i]
            i+=1

        return_string+=' '

    return return_string[:-1]

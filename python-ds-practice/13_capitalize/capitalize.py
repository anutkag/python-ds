def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    firstLetter= phrase[0].upper()
    restOfWord= phrase[1:]
    return firstLetter+ restOfWord
print (capitalize('python'))
print (capitalize('only first word'))
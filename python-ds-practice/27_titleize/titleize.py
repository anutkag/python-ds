def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    splitedBySpace =phrase.split(" ")
    result=[]
    for word in splitedBySpace:
        capitalized=word[0].upper()+word [1:].lower()
        result.append(capitalized)
    return " ".join(result)
print (titleize('oNLy cAPITALIZe fIRSt'))


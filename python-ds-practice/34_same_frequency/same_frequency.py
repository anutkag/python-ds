def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    frequency1={}
    frequency2={}
    for digit in str(num1):
        frequency1[digit]=str(num1).count(digit)
    for digit in str(num2):
        frequency2[digit]=str(num2).count(digit)
    return frequency1==frequency2
print (same_frequency(551122, 221515))
print ( same_frequency(321142, 3212215))
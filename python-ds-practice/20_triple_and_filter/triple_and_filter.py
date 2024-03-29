def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    filter=[]
    for num in nums:
        result= num * 3
        if result % 4==0:
            filter.append(num*3)
    return filter
print (triple_and_filter([6, 8, 10, 12]))
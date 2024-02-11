def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    #newList=[]
    #for item in lst:
       # if item:
            #newList.append(item)
    #return newList 
    return [item for item in lst if item ]
print (compact([0, 1, 2, '', [], False, (), None, 'All done']))

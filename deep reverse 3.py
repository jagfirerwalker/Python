def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    def getKey(item):
        try: 
            return item[0]
        except IndexError:
            return 0


    for i in range(len(L)):
        L[i].sort(key=abs)
        L[i].reverse() 
     
    
    
    return sorted(L, key=getKey, reverse=True) 
        
L = [[-1], []]
print(deep_reverse(L)) 
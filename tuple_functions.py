''' Several useful functions for doing things with tuples
 '''
#order does not matter with keyword arguments

def tuple_value_change_kw(a_tuple=(2,3,4,5),an_int=6):
    '''this function changes the 1st value of a tuple'''
    tupnew = (an_int,)
    '''newtuple[0:] gets the first value of the tuple'''
    tupnew = tupnew + a_tuple[0:]
    print tupnew + a_tuple[0:]
    return tupnew
#returns the lenght of tuples input
def tuplength( *tuple ):
    for i in tuple:
        print i
        print len (i)

    

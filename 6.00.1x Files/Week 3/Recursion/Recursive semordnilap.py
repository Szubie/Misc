#Using a "wrapper function" in order to check to make sure that the strings aren't the same, and that they are longer than 1 character.

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    elif len(str1) ==1:
        return str1 == str2
    else:
        return semordnilap(str1[1:], str2[0:len(str2)-1])
       #code below would work in an iterative loop if there was one. Above is the recursive form of it though.
       # if str1[0] == str2 [len(str2)-1]:
       #     str1 = str1[1:]
       #     str2 = str2[0:len(str2)-1]
       # else:
       #     return False
        


def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
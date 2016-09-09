""" Ye old prime number checker """


def isprime(mynum):

    if type(mynum) is not int:
        return False
    elif mynum <= 0:
        return False
    elif mynum == 1 or mynum == 2:
        return True
    elif mynum % 2 == 0:
        return False
    else:
        i=3
        while i < mynum:
            if mynum % i == 0:
                return False
            i += 2 

    return True

if __name__ == "__main__":
    print isprime(-1)   # False
    print isprime(2)    # True
    print isprime(1)    # True
    print isprime(7)    # True
    print isprime(3)    # True
    print isprime(8)    # False
    print isprime(365)  # False
    print isprime(13)   # True
    print isprime(45.6) # False
    print isprime('whoops') # False



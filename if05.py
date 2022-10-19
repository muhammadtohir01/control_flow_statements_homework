def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    x1=0
    x2=0
    x3=0
    if a<0:
        x1=1
    if b<0:
        x2=1
    if c<0:
        x3=1
    return x1+x2+x3
print(main(-3,3,-9))
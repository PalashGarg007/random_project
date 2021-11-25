def gcd(a, b):
    """ 
    gcd means greatest common diviser
    arguments = int a, int b
    
    BY Euclidean algorithm for computing the greatest common divisor
    1.  gcd(a, 0) == a
    2.  gcd(a, b) == gcd(b, a % b)
    
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

def binaryExponent(a,b):
    """ 
    arguments = int a , int b
    which returns a to the power of b; and has
    Time complaxicity = O(log(n))
    
    BY Binary Exponentiation algorithum:
        
    a^b = 1                      if:  b = 0
    a^b = [a^(b/2)]^2            if:  b > 0 and b is even
    a^b = {[a^[(b-1)/2]]^2}*a    if:  b > 0 and b is odd
    """
    
    if b==0 :
        return 1
    res = binaryExponent(a,b//2)
    if b%2 :
        return res*res*a
    else:
        return res*res


# def fibonacciSeries(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacciSeries(n-1) + fibonacciSeries(n-2)


from datetime import datetime
time_q1 = 0
for _ in range((100)):
    start = datetime.now()
    q1 = binaryExponent(1234567890, 34567)
    time_q1 += datetime.now() - start

time_q2 = 0
for _ in range((100)):
    start = datetime.now()
    q2 = pow(1234567890, 34567)
    time_q2 += datetime.now() - start

print(f"q1: {time_q1 // 100} \n q2: {time_q2 // 100}")

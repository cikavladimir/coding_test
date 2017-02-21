def percentile(N, P):
    """
    Find the percentile of a list of values

    @parameter N - A list of values.  N must be sorted.
    @parameter P - A float value from 0.0 to 1.0

    @return - The percentile of the values.
    """
    n = int(round(P * len(N) + 0.5))
    return N[n-1]

# A = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# B = (15, 20, 35, 40, 50)
#
# print percentile(A, P=0.3)
# 4
# print percentile(A, P=0.8)
# 9
# print percentile(B, P=0.3)
# 20
# print percentile(B, P=0.8)
# 50




import numpy as np
a = [154, 400, 1124, 82, 94, 108]
print np.percentile(a,95) # gives the 95th percentile
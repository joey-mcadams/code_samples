#!/bin/python3

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1 - Position 1st Kangaroo
#  2. INTEGER v1 - Velocity 1st Kangaroo
#  3. INTEGER x2 - Position 2nd Kangaroo
#  4. INTEGER v2 - Velocity 2nd Kangaroo
#

def kangaroo(x1, v1, x2, v2):
    """
    Given the position and velocity (how far they jump) of each kangaroo
    return if they'll ever be at the same spot at the same time.
    """
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        if v1 != v2 and (x2 - x1) % (v2 - v1) == 0:
            return 'YES'
        else:
            return 'NO'

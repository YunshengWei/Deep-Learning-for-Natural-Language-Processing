##
# Miscellaneous helper functions
##

from numpy import *

def random_weight_matrix(m, n):
    #### YOUR CODE HERE ####
    epsilon = np.sqrt(6 / (m + n))
    A0 = 2 * epsilon * random.rand((m, n)) - epsilon
    #### END YOUR CODE ####
    
    assert(A0.shape == (m,n))
    return A0
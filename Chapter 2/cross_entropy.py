import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    """
    result = []
    for i,j in Y,P:
        exist = np.float_(i)
        prob  = np.float_(j)
        result.extend(-np.sum(exist*(np.ln(prob)) + (1-exist)*(np.ln(1-prob))))
    return result

#pass"""
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.

#list = [5,3,8]
result = []
def softmax(L):
        expl = np.exp(L)
        sumExp = sum(expl)
        for i in expl:
            answer = (i/sumExp)
            result.append(answer)
        return result
#pass

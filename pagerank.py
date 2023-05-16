import numpy as np

internet = [
        [0,1],
        [2,3,4],
        [3,4],
        [3,4],
        [0,3]
    ]

n = 5
transmat = np.zeros((n,n))
for idx,nbrs in enumerate(internet):
    transmat[nbrs,idx] = 1/len(nbrs)

v = np.array([1,0,0,0,0])
transmat@v

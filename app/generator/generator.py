import numpy as np
from random import random, randrange, randint

class Generator:
    def create_matrix(self):
        gen_matrix=np.zeros((randint(5,8),randint(5,8)))
        size_gen_matrix = gen_matrix.shape
        for col in range(0,size_gen_matrix[0]):
            rnd=randint(0,size_gen_matrix[0])
            np.place(gen_matrix[col,:rnd], gen_matrix[col, :rnd] == 0, 1)
        return gen_matrix
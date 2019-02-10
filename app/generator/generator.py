import numpy as np
from random import randint


class Generator:
    def create_matrix_rnd(self):
        gen_matrix = np.zeros((randint(5, 6), randint(5, 6)))
        size_gen_matrix = gen_matrix.shape
        for col in range(0, size_gen_matrix[0]):
            rnd = randint(0, size_gen_matrix[0])
            np.place(gen_matrix[col, :rnd], gen_matrix[col, :rnd] == 0, 1)
        print(gen_matrix)
        return gen_matrix

# генератор массива
import numpy as np
from random import randint


class Generator:
    def __init__(self):
        self.__get_matrix= np.array([], dtype=int)
    def __create_matrix_rnd(self):
        self.__get_matrix = np.zeros((randint(5, 6), randint(5, 6)))
        size_gen_matrix = self.__get_matrix.shape
        for col in range(0, size_gen_matrix[0]):
            rnd = randint(0, size_gen_matrix[0])
            np.place(self.__get_matrix[col, :rnd], self.__get_matrix[col, :rnd] == 0, 1)
        print(self.__get_matrix)
        return self.__get_matrix

    @property
    def getGenerator(self):
        self.__create_matrix_rnd()
        return self.__get_matrix

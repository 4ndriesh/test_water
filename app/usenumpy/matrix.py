"""
1. Прохожу по массиву и соединяю воду между возвышенностями;
2. Нахожу нулевые ячейки в нижней строке и в крайних столбцах, затем удаляю все связанные ячейки.
[[1. 1. 0. 0. 0. 0.]
 [1. 1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 0. 0.]
 [1. 1. 1. 1. 0. 0.]
 [1. 1. 0. 0. 0. 0.]
 [1. 1. 1. 1. 0. 0.]]
 
[[ 1.  1.  0.  0.  0.  0.]
 [ 1.  1.  1.  1.  1.  1.]
 [ 0.  0.  0.  0.  0.  0.]
 [ 1.  1.  1.  1.  0.  0.]
 [ 1.  1. 44. 34.  0.  0.]
 [ 1.  1.  1.  1.  0.  0.]]
 
 
"""
import numpy as np


class Matrix:
    def __init__(self):
        pass
        self.__obj_with_water = np.array([], dtype=int)

    def __delete_water_last_row(self, row_matrix):
        for col, delete in enumerate(row_matrix, 0):
            if delete == 0: continue
            arr = self.__obj_with_water[:, col]
            np.place(arr, arr == delete, 0)

        print(self.__obj_with_water)
        return self.__obj_with_water

    def __change_matrix(self, mass):
        self.__obj_with_water = mass
        self.size_matrix = self.__obj_with_water.shape
        water = 11
        for i, col in enumerate(reversed(range(self.size_matrix[1])), 1):
            row = 0
            for j, row in enumerate(range(0, self.size_matrix[0]), 1):
                if col == 0 and self.__obj_with_water[row][col] == 0:
                    obj_with_water = self.__delete_water_last_row(self.__obj_with_water[row, :])
                    continue

                elif self.__obj_with_water[row][col] == 0:
                    if row == 0:
                        water = 0
                        continue
                    self.__obj_with_water[row][col] = water
                else:
                    water = int("{0}{1}".format(i, j))
            if self.__obj_with_water[row, col] == water:
                arr = self.__obj_with_water[:, col]
                np.place(arr, arr == water, 0)

    @property
    def get_obj_with_water(self):
        return self.__obj_with_water.tolist()

    @get_obj_with_water.setter
    def get_obj_with_water(self, mass):
        self.__change_matrix(mass)

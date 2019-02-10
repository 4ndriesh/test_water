import numpy as np


class Matrix:
    def __init__(self, gen):
        self.new_matrix = np.array(gen)
        self.obj_with_water = np.flipud(self.new_matrix.transpose())
        self.size_matrix = self.obj_with_water.shape
        print(self.obj_with_water)

    def change_matrix(self):

        water = '11'
        for i, row in enumerate(range(0, self.size_matrix[0]), 1):
            for j, col in enumerate(range(0, self.size_matrix[1]), 1):
                if self.obj_with_water[row][col] == 0:
                    self.obj_with_water[row][col] = water
                else:
                    water = "{0}{1}".format(i, j)

        print(self.obj_with_water)

    def delete_water_last_col(self, col):
        for col, delete in enumerate(col, 0):
            if delete != 1:
                np.place(self.obj_with_water[col, :], self.obj_with_water[col, :] == delete, 0)

    def delete_water_last_row(self):
        for col, delete in enumerate(self.obj_with_water[self.size_matrix[0] - 1, :], 0):
            if delete != 1:
                for irow, row in enumerate(self.obj_with_water[:, col]):
                    np.place(self.obj_with_water[irow, :], self.obj_with_water[irow, :] == row, 0)

        self.delete_water_last_col(self.obj_with_water[:, self.size_matrix[1] - 1])
        self.delete_water_last_col(self.obj_with_water[:, 0])
        print(self.obj_with_water)
        return np.flipud(self.obj_with_water)

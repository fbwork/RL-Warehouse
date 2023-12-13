import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


class DrawGrid:
    def __init__(self, start_index, aisles, path, packaging_area, environment_rows, environment_columns):
        self.aisles = aisles
        self.start_index = start_index
        self.path = path
        self.packaging_area = packaging_area
        self.grid = np.full((environment_rows, environment_columns), 1)
        self.update_grid()

    def update_grid(self):
        self.grid[self.start_index] = 0
        self.grid[self.packaging_area] = 3
        # set the rewards for all aisle locations (i.e., white squares)
        for row_index in range(1, 10):
            for column_index in self.aisles[row_index]:
                self.grid[row_index, column_index] = 2
        for i in self.path:
            self.grid[tuple(i)] = 0

    def draw(self):
        # create discrete colormap
        cmap = colors.ListedColormap(['green', 'black', 'white'])
        bounds = [0, 1, 2, 3]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(self.grid, cmap=cmap, norm=norm)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, 10, 1));
        ax.set_yticks(np.arange(-.5, 10, 1));
        plt.tick_params(bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False)
        plt.show()

import time

from grid import DrawGrid

import settings
from play import Play


def train():
    obj_play = Play(settings.ENVIRONMENT_ROWS, settings.ENVIRONMENT_COLUMNS, settings.PACKAGING_AREA)
    obj_play.train()
    print('Training complete!')
    display(obj_play)


def display(play):
    # display a few shortest paths
    # starting at row 3, column 9
    path = play.get_shortest_path(3, 9)
    print(path)
    obj_grid = DrawGrid((3, 9), play.environment.aisles, path, settings.PACKAGING_AREA, settings.ENVIRONMENT_ROWS,
                        settings.ENVIRONMENT_COLUMNS)
    obj_grid.draw()
    time.sleep(5)
    # starting at row 5, column 0
    path = play.get_shortest_path(5, 0)
    print(path)
    obj_grid = DrawGrid((5, 0), play.environment.aisles, path, settings.PACKAGING_AREA, settings.ENVIRONMENT_ROWS,
                        settings.ENVIRONMENT_COLUMNS)
    obj_grid.draw()
    time.sleep(5)
    # starting at row 9, column 5
    path = play.get_shortest_path(9, 5)
    print(path)
    obj_grid = DrawGrid((9, 5), play.environment.aisles, path, settings.PACKAGING_AREA, settings.ENVIRONMENT_ROWS,
                        settings.ENVIRONMENT_COLUMNS)
    obj_grid.draw()
    time.sleep(5)


if __name__ == '__main__':
    train()

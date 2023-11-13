import settings
from play import Play


def train():
    obj_play = Play(settings.ENVIRONMENT_ROWS, settings.ENVIRONMENT_COLUMNS)
    obj_play.train()
    print('Training complete!')
    display(obj_play)


def display(play):
    # display a few shortest paths
    print(play.get_shortest_path(3, 9))  # starting at row 3, column 9
    print(play.get_shortest_path(5, 0))  # starting at row 5, column 0
    print(play.get_shortest_path(9, 5))  # starting at row 9, column 5

    # display an example of reversed shortest path
    path = play.get_shortest_path(5, 2)  # go to row 5, column 2
    path.reverse()
    print(path)


if __name__ == '__main__':
    train()

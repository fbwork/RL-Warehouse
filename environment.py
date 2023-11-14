import numpy as np


class Environment:
    def __init__(self, environment_rows, environment_columns):
        """
        initialize the environment
        :param int environment_rows: number of rows
        :param int environment_columns: number of columns
        :return: None
        """
        # define the shape of the environment (i.e., its states)
        self.environment_rows = environment_rows
        self.environment_columns = environment_columns

        # Create a 3D numpy array to hold the current Q-values for each state and action pair: Q(s, a)
        # The array contains 11 rows and 11 columns (to match the shape of the environment),
        # as well as a third "action" dimension.
        # The "action" dimension consists of 4 layers that will allow us
        # to keep track of the Q-values for each possible action in
        # each state (see next cell for a description of possible actions).
        # The value of each (state, action) pair is initialized to 0.
        self.q_values = np.zeros((self.environment_rows, self.environment_columns, 4))

        # define actions
        # numeric action codes: 0 = up, 1 = right, 2 = down, 3 = left
        self.actions = ['up', 'right', 'down', 'left']

        # Create a 2D numpy array to hold the rewards for each state.
        # The array contains 11 rows and 11 columns
        # (to match the shape of the environment), and each value is initialized to -100.
        self.rewards = np.full((environment_rows, environment_columns), -100.)

        # store locations in a dictionary
        self.aisles = {}
        self.def_aisle()
        self.update_rewards()

    def def_aisle(self):
        # define aisle locations (i.e., white squares) for rows 1 through 9
        self.aisles[1] = [i for i in range(1, 10)]
        self.aisles[2] = [1, 7, 9]
        self.aisles[3] = [i for i in range(1, 8)]
        self.aisles[3].append(9)
        self.aisles[4] = [3, 7]
        self.aisles[5] = [i for i in range(11)]
        self.aisles[6] = [5]
        self.aisles[7] = [i for i in range(1, 10)]
        self.aisles[8] = [3, 7]
        self.aisles[9] = [i for i in range(11)]

    def update_rewards(self):
        # set the reward for the packaging area (i.e., the goal) to 100
        self.rewards[0, 5] = 100.
        # set the rewards for all aisle locations (i.e., white squares)
        for row_index in range(1, 10):
            for column_index in self.aisles[row_index]:
                self.rewards[row_index, column_index] = -1.

        # print rewards matrix
        for row in self.rewards:
            print(row)

import numpy as np

import settings
from environment import Environment


class Play:
    def __init__(self, environment_rows, environment_columns, packaging_area):
        self.environment = Environment(environment_rows, environment_columns, packaging_area)

    # define a function that determines if the specified location is a terminal state
    def is_terminal_state(self, current_row_index, current_column_index):
        # if the reward for this location is -1, then it is not a terminal state (i.e., it is a 'white square')
        if self.environment.rewards[current_row_index, current_column_index] == -1.:
            return False
        else:
            return True

    # define a function that will choose a random, non-terminal starting location
    def get_starting_location(self):
        # get a random row and column index
        current_row_index, current_column_index = self.get_random_location()
        # continue choosing random row and column indexes until a non-terminal state is identified
        # (i.e., until the chosen state is a 'white square').
        while self.is_terminal_state(current_row_index, current_column_index):
            current_row_index, current_column_index = self.get_random_location()
        return current_row_index, current_column_index

    def get_random_location(self):
        random_row_index = np.random.randint(self.environment.environment_rows)
        random_column_index = np.random.randint(self.environment.environment_columns)
        return random_row_index, random_column_index

    # define an epsilon greedy algorithm that will choose which action to take next (i.e., where to move next)
    def get_next_action(self, current_row_index, current_column_index, epsilon=settings.EPSILON):
        # if a randomly chosen value between 0 and 1 is less than epsilon,
        # then choose the most promising value from the Q-table for this state.
        if np.random.random() < epsilon:
            return np.argmax(self.environment.q_values[current_row_index, current_column_index])
        else:  # choose a random action
            return np.random.randint(4)

    # define a function that will get the next location based on the chosen action
    def get_next_location(self, current_row_index, current_column_index, action_index):
        new_row_index = current_row_index
        new_column_index = current_column_index
        if self.environment.actions[action_index] == 'up' and current_row_index > 0:
            new_row_index -= 1
        elif self.environment.actions[action_index] == 'right' and \
                current_column_index < self.environment.environment_columns - 1:
            new_column_index += 1
        elif self.environment.actions[action_index] == 'down' and \
                current_row_index < self.environment.environment_rows - 1:
            new_row_index += 1
        elif self.environment.actions[action_index] == 'left' and current_column_index > 0:
            new_column_index -= 1
        return new_row_index, new_column_index

    # Define a function that will get the shortest path between any location within the warehouse that
    # the robot is allowed to travel and the item packaging location.
    def get_shortest_path(self, start_row_index, start_column_index):
        print("-" * 20)
        print(f'Shortest path from [{start_row_index}, {start_column_index}]: ')
        # return immediately if this is an invalid starting location
        if self.is_terminal_state(start_row_index, start_column_index):
            return []
        else:  # if this is a 'legal' starting location
            current_row_index, current_column_index = start_row_index, start_column_index
            shortest_path = list()
            shortest_path.append([current_row_index, current_column_index])
            # continue moving along the path until we reach the goal (i.e., the item packaging location)
            while not self.is_terminal_state(current_row_index, current_column_index):
                # get the best action to take
                action_index = self.get_next_action(current_row_index, current_column_index, 1.)
                # move to the next location on the path, and add the new location to the list
                current_row_index, current_column_index = self.get_next_location(current_row_index,
                                                                                 current_column_index, action_index)
                shortest_path.append([current_row_index, current_column_index])
            return shortest_path

    def train(self):
        # run through 1000 training episodes
        for episode in range(1000):
            # print(f'Training episode {episode} ...')
            # get the starting location for this episode
            row_index, column_index = self.get_starting_location()

            # continue taking actions (i.e., moving) until we reach a terminal state
            # (i.e., until we reach the item packaging area or crash into an item storage location)
            while not self.is_terminal_state(row_index, column_index):
                # choose which action to take (i.e., where to move next)
                action_index = self.get_next_action(row_index, column_index)

                # perform the chosen action, and transition to the next state (i.e., move to the next location)
                old_row_index, old_column_index = row_index, column_index  # store the old row and column indexes
                row_index, column_index = self.get_next_location(row_index, column_index, action_index)

                # receive the reward for moving to the new state, and calculate the temporal difference
                reward = self.environment.rewards[row_index, column_index]
                old_q_value = self.environment.q_values[old_row_index, old_column_index, action_index]
                temporal_difference = reward + (settings.DISCOUNT_FACTOR * np.max(
                    self.environment.q_values[row_index, column_index])) - old_q_value

                # update the Q-value for the previous state and action pair
                new_q_value = old_q_value + (settings.LEARNING_RATE * temporal_difference)
                self.environment.q_values[old_row_index, old_column_index, action_index] = new_q_value

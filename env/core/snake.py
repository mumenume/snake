import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        self.head_position = head_position
        self.direction_index = direction_index
        self.length = length

        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        """
        @param action: int
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        direction = self.current_direction_index

        if (abs(direction - action)) == 1 or (abs(direction - action)) == 3:
            self.current_direction_index = action
        #elif (abs(direction - action)) == 2:
        #    return
        # Remove tail
        tail = self.blocks[-1]
        self.blocks.remove(tail)
        # Check new head
        new_head = np.array(self.head_position) + DIRECTIONS[self.current_direction_index]
        self.head_position = new_head
        # Add new head
        self.blocks = [tuple(new_head)] + self.blocks
        return tuple(new_head), tail

# Sasha = Snake((10, 10), 2, 10)
# print(Sasha.blocks)
# print(Sasha.step(1))
# print(Sasha.blocks)
# print(Sasha.step(0))
# print(Sasha.blocks)
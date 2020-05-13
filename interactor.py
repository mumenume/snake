import sys, tty, select
import random

from env.snake_env import SnakeEnv


def interact():
    """
    Human interaction with the environment
    """
    tty.setcbreak(sys.stdin)
    env = SnakeEnv()
    done = False
    r = 0
    action = random.randrange(4)

    while not done:
        pressed, _, _ = select.select([sys.stdin], [], [], 0.5)
        if pressed:
            key = sys.stdin.read(1)
            # up
            if key == 'w':
                action = 0
            # down
            elif key == 's':
                action = 2
            # left
            elif key == 'a':
                action = 3
            # right
            elif key == 'd':
                action = 1

        obs, reward, done, info = env.step(action)
        env.render(mode='human')
        r += reward
    return r


if __name__ == '__main__':
    interact()
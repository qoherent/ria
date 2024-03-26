"""
A simple looping function with one python package requirement
"""
from tqdm import tqdm


def simple_loop_func(number):
    """
    Using tqdm progress bar this function prints out the progress of the for loop
    :param number: int digit to be the end of the for loop
    """
    for _ in tqdm(range(number)):
        pass


def __ignored_func():
    print("This is an ignored function and this message will not be printed")


if __name__ == '__main__':
    print("This is a progress bar of the simple loop script")
    simple_loop_func(1000000)
import time
from typing import List, Tuple, Union

from boggle_board_randomizer import randomize_board

STEP_LIST = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0),
             (-1, -1)]

ROW = 0
COL = 1
MIN_WORD_LEN = 3
MAX_WORD_LEN = 16


def load_words_dict(
        file_path: str = "boggle_dict.txt") -> dict:
    """
    loads words from a given .txt file and uses them as keys in a dictionary
    with all values being True
    :param file_path: the path to the file with the word
    :return: a dictionary of form {word_from_file : True}
    """
    words_dict = dict()
    with open(file_path) as f:
        for line in f:
            if line:
                words_dict[str(line.rstrip('\n'))] = True
    return words_dict


def is_valid_path(board: List[List[str]],
                  path: List[Tuple[int, int]],
                  words: dict):
    """
    checks if a list of coordinates is valid as a path in the game
    :param board: the board of the game
    :param path: a list of coordinate tuples
    :param words: a dictionary of words that are possible in the game
    :return: None if path is not valid or if path doesn't match a word from
    words, else - the word the path indicates
    """
    if not path or len(path) != len(set(path)) or \
            len(path) not in range(0, 17):  # if path is empty or repetitive or
        # not a valid length
        return
    for i in range(len(path) - 1):  # checks for step validity
        if not is_distance_valid(path[i], path[i + 1]):
            return
    path_str = ""
    for coordinate in path:
        if coordinate[0] < 0 or coordinate[0] > len(board) - 1 or \
                coordinate[1] < 0 or coordinate[1] > len(board[0]) - 1:
            # checks that the path is in the board
            return
        path_str += board[coordinate[0]][coordinate[1]]
    return path_str if path_str in words else None


def is_distance_valid(coord_a: Tuple[int, int],
                      coord_b: Tuple[int, int]) -> bool:
    """
    checks if two coordinates a adjutant
    :param coord_a: the first coordinate
    :param coord_b: the first coordinate
    :return: True if the coordinates are adjutant, False if not
    """
    return True if (coord_a[ROW] - coord_b[ROW],
                    coord_a[COL] - coord_b[COL]) in STEP_LIST else False


def find_length_n_words(n: int, board: List[List[str]], words: dict) -> \
        Union[List[Tuple[str, Tuple]], None]:
    """
    finds all words with paths with length n in the given board
    :param n: the length of the path of the word
    :param board: the 2D list of the board
    :param words: a dictionary with words to search in on the board
    :return: a list of tuples where each tuple is (<word>,[<list of tuples
    of path>])
    """
    if not words or not board or not board[0]:
        return []
    if n < 3 or n > 16:
        return []
    board_coordinates = [(i, j) for i in range(len(board)) for j in range(len(
        board[0]))]  # generate tuples for all coordinates on the board
    valid_words_in_board = []
    for path in modified_permutations(board_coordinates, n):  # gets a list
        # of coordinate tuples for the path
        possible_word = ""
        for coord in path:  # crates the word
            possible_word += board[coord[0]][coord[1]]  # finds the word of
            # the path
        if possible_word in words:  # checks compatibility
            new_found_word = (possible_word, list(path))
            valid_words_in_board.append(new_found_word)
    return valid_words_in_board if valid_words_in_board else []


def modified_permutations(iterable, r=None):
    """
    a modification of permutations from itertools for getting all
    permutations of valid paths on the board
    :param iterable: the board
    :param r: the length of the searched word
    :return: a tuple of coordinate tuples
    """
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in range(r))  # yields first path
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                for_y = tuple(pool[i] for i in indices[:r])
                checker = 0
                for t in range(len(for_y) - 1):
                    if is_distance_valid(for_y[t], for_y[t + 1]):  # checks
                        # for no exceptions from rulse
                        checker += 1
                if checker == r - 1:
                    yield for_y
                break
        else:
            return


if __name__ == "__main__":
    # TODO remove

    pass
    rand_board = randomize_board()
    word_dict = load_words_dict()
    # coords_in_board = [(i, j) for i in range(len(rand_board)) for j in
    #                    range(len(
    #                        rand_board[0]))]
    # # print(list(permutations(coords_in_board, 3)))
    # # print(list(permutations(coords_in_board[:][::-1], 3)))
    # # if ((3, 3), (3, 2), (3, 1)) in coords_in_board:
    # #     print("!")
    for p in range(10):
        y = time.time()
        find_length_n_words(p, rand_board, word_dict)
        x = time.time()
        find_length_n_words(p, rand_board, word_dict)
        z = time.time()
        find_length_n_words(p, rand_board, word_dict)
        w = time.time()
        avg = ((x - y) + (z - x) + (w - z)) / 3
        print(f"n = {p} took on average:", avg,
              "specifically:", x - y, z - x, w - z)
    # per = list(modified_permutations(((0, 0), (0, 1), (0, 2), (0, 3),
    #                                   (1, 0), (1, 1), (1, 2), (1, 3),
    #                                   (2, 0), (2, 1), (2, 2), (2, 3),
    #                                   (3, 0), (3, 1), (3, 2), (3, 3)), 5))
    # print("lst_len:", len(per))
    # # print("per_lst", per)
    # print("set_len:", len(set(per)))
    # # print(set(per))
    # if ((2, 2), (0, 1), (1, 2)) in set(per):
    #     print("!")

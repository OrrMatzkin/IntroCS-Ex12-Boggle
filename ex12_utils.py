#################################################################
# FILE : ex12_utils.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs2 ex12 2020
# DESCRIPTION: the main program for the boggle program
# STUDENTS WE DISCUSSED THE EXERCISE WITH:
# WEB PAGES WE USED:
#################################################################

import copy
from typing import List, Tuple, Union, Dict

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


def find_length_n_words(n: int, board: List[List[str]],
                        words: dict):
    """
    calls the appropriate find_n_length_words where recursive is faster than
    not recursive for n > 4
    :param n: the length of the required word
    :param board: a 2D list of letters
    :param words: a dictionary with the words as keys
    :return: the list of tuples of words that have been found
    and their coordinates
    """
    if n < 5:
        return not_recursive_find_length_n_words(n, board, words)
    else:
        return recursive_find_length_n_words(n, board, words)


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


def search_words(curr_board: List[List[str]],
                 curr_row: int,
                 curr_col: int,
                 words_dict: Dict,
                 word_remaining_len: int,
                 curr_coordinates: Union[List[Tuple[int, int]], List],
                 found_word_lst: Union[Tuple[str, Union[List[Tuple[int, int]],
                                                        List]], List],
                 curr_str: str,
                 required_word_length: int) -> \
        Union[Tuple[str, Union[List[Tuple[int, int]], List]], List, None]:
    """
    recursively goes through all possible solutions for the current board
    with the given words from the word dictionary, the given desired length
    for the word and while abiding to the rules of the game
    :param required_word_length: the required length of the word
    :param word_remaining_len: the number of remaining letters the gather for
    the word
    :param curr_board: the board to search on
    :param curr_row: current x position in the board
    :param curr_col: current x position in the board
    :param words_dict: the dictionary of possible word to find
    :param curr_coordinates: the list of all coordinates visited in current
    path
    :param found_word_lst: the list of tuples of words that have been found
    and their coordinates
    :param curr_str: the string created in the current path
    :return: the found_word_lst of all the routs starting with the current
    starting place
    """
    if curr_row < 0 or curr_row > len(curr_board) - 1 or \
            curr_col < 0 or curr_col > len(curr_board[0]) - 1:  # if out of
        # the board
        return
    if word_remaining_len < 0:  # if reached maximum word length
        return

    if curr_board[curr_row][curr_col] != "_":  # if had not been here before
        word_remaining_len -= 1
        if word_remaining_len < 0:
            return
        new_str = curr_str + curr_board[curr_row][curr_col]
        new_coords = curr_row, curr_col
        new_board = copy.deepcopy(curr_board)
        new_board[curr_row][curr_col] = "_"
        new_coordinates_lst = copy.deepcopy(curr_coordinates)
        new_coordinates_lst.append(new_coords)
        new_dict = {key: value for (key, value) in words_dict.items() if
                    new_str in key and len(key) >= required_word_length}
        if not new_dict:  # if no matching words in the dict for the current
            # str
            return
        if new_str in new_dict.keys() and len(new_coordinates_lst) == \
                required_word_length:  # if found a word
            found_word_tuple = new_str, new_coordinates_lst
            found_word_lst.append(tuple(found_word_tuple))
        else:
            for next_row, next_col in STEP_LIST:  # take next step
                search_words(new_board,
                             curr_row + next_row,
                             curr_col + next_col,
                             new_dict,
                             word_remaining_len,
                             new_coordinates_lst,
                             found_word_lst,
                             new_str,
                             required_word_length)
        return found_word_lst


def recursive_find_length_n_words(n: int, board: List[List[str]],
                                  words: dict) -> Union[List, None]:
    """
    finds all possible words with given length n in the board and returns a
    list of tuples (word,[list of coordinates for the path])
    :param n: the length of the required word
    :param board: a 2D list of letters
    :param words: a dictionary with the words as keys
    :return: the list of tuples of words that have been found
    and their coordinates
    """
    if not words:
        return []
    if n not in range(MIN_WORD_LEN, MAX_WORD_LEN + 1):
        return []
    found_words_list = []
    for i in range(len(board) * len(board[0])):  # loops for each tile in the
        row, col = i // len(board), i % len(board[0])
        new_found_lst = search_words(curr_board=board,
                                     curr_row=row,
                                     curr_col=col,
                                     words_dict=words,
                                     word_remaining_len=n,
                                     curr_coordinates=[],
                                     found_word_lst=[],
                                     curr_str="",
                                     required_word_length=n)
        if new_found_lst:
            found_words_list.extend(new_found_lst)
    return found_words_list


def not_recursive_find_length_n_words(n: int,
                                      board: List[List[str]],
                                      words: dict) -> \
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
                        # for no exceptions from rules
                        checker += 1
                if checker == r - 1:
                    yield for_y
                break
        else:
            return


if __name__ == "__main__":
    pass

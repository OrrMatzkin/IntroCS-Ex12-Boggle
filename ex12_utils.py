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
                words_dict[line[:-2]] = True
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
            len(path) not in range(3, 17):  # if path is empty or repetitive or
        # not a valid length
        return
    for i in range(len(path) - 1):  # checks for step validity
        if abs(path[i][ROW] - path[i + 1][ROW]) != 1 and \
                abs(path[i][COL] - path[i + 1][COL]) != 1:
            return
    path_str = ""
    for coordinate in path:
        if coordinate[0] < 0 or coordinate[0] > len(board) - 1 or \
                coordinate[1] < 0 or coordinate[1] > len(board[0]) - 1:
            # checks that the path is in the board
            return
        path_str += board[coordinate[0]][coordinate[1]]
    return path_str if path_str in words else None


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
    if len(found_word_lst) > 3:  # TODO add parameter for game
        return found_word_lst
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
        if not new_dict:  # if no
            # matching words in the dict for the current str
            print("not any")
            return
        print("are any")
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


def find_length_n_words(n: int, board: List[List[str]], words: dict) -> \
        Union[List, None]:
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
        return
    if n not in range(MIN_WORD_LEN, MAX_WORD_LEN + 1):
        return
    found_words_list = []
    for i in range(len(board) * len(board[0])):  # loops for each tile in the
        # board
        if len(found_words_list) > 5:  # TODO remove
            return found_words_list
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

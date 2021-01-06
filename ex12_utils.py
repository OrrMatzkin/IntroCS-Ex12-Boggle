import copy
from typing import List, Tuple, Union
from boggle_board_randomizer import *

STEP_LIST = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0),
             (-1, -1)]


def load_words_dict(
        file_path: str) -> dict:  # TODO check if need to raise special error
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


def is_valid_path(board, path, words):
    pass


def get_neighbors(board, row, col):
    neighbors_lst = [[board[j][i], (j, i)] for j in
                     range(col - 2, col + 1) for i in
                     range(row - 2, row + 1) if 0 <= i < 4 and 0 <= j < 4
                     and board[j][i] != board[row - 1][col - 1]]
    return neighbors_lst


def search_words(curr_board: List[List[str]],
                 curr_row: int,
                 curr_col: int,
                 words_lst: List[str],
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
    :param words_lst: the list of possible word to find (from dictionary
    with the correct length)
    :param curr_coordinates: the list of all coordinates visited in current
    path
    :param found_word_lst: the list of tuples of words that have been found
    and their coordinates
    :param curr_str: the string created in the current path
    :return: the found_word_lst of all the routs starting with the current
    starting place
    """

    if curr_row in (-1, len(curr_board)) or curr_col in (-1, len(curr_board[
                                                                     0])):
        # if out of the board
        return
    if word_remaining_len < 0:  # if reached maximum word length
        return
    if curr_board[curr_row][curr_col]:  # if had not been here before
        word_remaining_len -= 1
        if word_remaining_len < 0:
            return
        new_str = curr_str + curr_board[curr_row][curr_col]
        new_coords = curr_row, curr_col
        new_board = copy.deepcopy(curr_board)
        new_board[curr_row][curr_col] = ""
        new_coordinates_lst = copy.deepcopy(curr_coordinates)
        new_coordinates_lst.append(new_coords)

        if new_str in words_lst and len(new_coordinates_lst) == \
                required_word_length:  # if found a word
            found_word_tuple = new_str, new_coordinates_lst
            found_word_lst.append(tuple(found_word_tuple))

        for next_row, next_col in STEP_LIST:  # take next step
            search_words(new_board,
                         curr_row + next_row,
                         curr_col + next_col,
                         words_lst,
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
    words_lst = [key for key in words]  # creates a list from the words in the
    # dictionary
    if not words_lst:
        return
    found_words_list = []
    for i in range(BOARD_SIZE ** 2):  # loops for each tile in the board
        row, col = i // len(board), i % len(board[0])
        found_words_list.extend(search_words(curr_board=board,
                                             curr_row=row,
                                             curr_col=col,
                                             words_lst=words_lst,
                                             word_remaining_len=n,
                                             curr_coordinates=[],
                                             found_word_lst=[],
                                             curr_str="",
                                             required_word_length=n))
    return found_words_list


if __name__ == "__main__":
    pass
# for _ in range(16):
#     b = randomize_board()
#     print(b)
#     print(find_length_n_words(3, b, load_words_dict("boggle_dict.txt")))

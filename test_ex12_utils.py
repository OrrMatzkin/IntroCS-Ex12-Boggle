from ex12_utils import *

B = [["A", 'B', "C", "D"],
     ["E", "F", "G", "H"],
     ["I", "J", "K", "L"],
     ["M", "N", "O", "P"]]

D = [["A", 'B', "C", "D", "H"],
     ["E", "F", "G", "H", "R"],
     ["I", "J", "K", "L", "0"],
     ["M", "N", "O", "P", "/"],
     ["AE", "TRE", "W", "Z", "RE"]]

A = [["A"]]

C = [["A", "B", "C", "D"]]

E = [["A"],
     ["E"],
     ["AJR"]]

WORDS1 = {"ABCD": True, "EFGK": True, "PON": True, "N": True,
          "ABCDHLPON": True}
WORDS2 = {"ABCD": True, "AEMNWTRE": True, "PON": True, "N": True,
          "ABCDHRHLPON": True}
WORDS3 = {"AB": True, "ABC": True}
SLASH_DICT = {"/": True}

LONG_COORD1 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2),
               (3, 1)]
LONG_COORD2 = [(4, 0), (3, 0), (3, 1), (4, 2), (4, 1)]
LONG_COORD3 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (2, 3),
               (3, 3), (3, 2), (3, 1)]

B4WORDS1 = [("ABCD", [(0, 0), (0, 1), (0, 2), (0, 3)]),
            ("EFGK", [(1, 0), (1, 1), (1, 2), (2, 2)])]
B3WORDS1 = [("PON", [(3, 3), (3, 2), (3, 1)])]
B1WORDS1 = [("N", [(3, 1)])]
B9WORDS1 = [("ABCDHLPON", LONG_COORD1)]


def test_is_valid_path_4board():
    assert not is_valid_path(B, [], WORDS1)
    assert not is_valid_path(B, [(1, 1)], WORDS1)
    assert not is_valid_path(B, [(-1, -1)], WORDS1)
    assert not is_valid_path(B, [(-1, 1)], WORDS1)
    assert not is_valid_path(B, [(1, -1)], WORDS1)
    assert not is_valid_path(B, [(1, 1), (2, 2), (3, 3)], WORDS1)
    assert is_valid_path(B, [(1, 1), (2, 2), (3, 3)], {"FKP": True}) == "FKP"
    assert is_valid_path(B, [(0, 0), (0, 1), (0, 2), (0, 3)], WORDS1) == "ABCD"
    assert is_valid_path(B, [(1, 0), (1, 1), (1, 2), (2, 2)], WORDS1) == "EFGK"
    assert is_valid_path(B, [(3, 3), (3, 2), (3, 1)], WORDS1) == "PON"
    # assert is_valid_path(B, [(3, 1)], WORDS1) == "N"
    assert is_valid_path(B, LONG_COORD1, WORDS1) == "ABCDHLPON"
    assert not is_valid_path(B, [(0, 0), (2, 2)], {"AK": True})
    assert not is_valid_path(B, [(4, 0)], {"AK": True})
    assert not is_valid_path(B, [(0, 4)], {"AK": True})
    assert not is_valid_path(B, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 2)],
                             WORDS1)
    assert not is_valid_path(B, [(-2, 4), (-1, 4)], {"AK": True})


def test_is_valid_path_5board():
    assert not is_valid_path(D, [(1, 1), (2, 2), (3, 3)], WORDS2)
    # assert is_valid_path(D, [(2, 4)], {"0": True}) == "0"
    assert is_valid_path(D, LONG_COORD2, WORDS2) == "AEMNWTRE"
    # assert is_valid_path(D, [(3, 4)], SLASH_DICT) == "/"
    assert is_valid_path(D, LONG_COORD3, WORDS2) == "ABCDHRHLPON"
    assert not is_valid_path(D, [(5, 0)], WORDS2)
    assert not is_valid_path(D, [(0, 5)], WORDS2)


# def test_is_valid_path_1board():
#     assert not is_valid_path(A, [(1, 1)], WORDS2)
#     assert is_valid_path(A, [(0, 0)], {"A": True}) == "A"
#     assert not is_valid_path(A, [], {"A": True})
#     assert not is_valid_path(A, [(1, 0)], WORDS1)
#     assert not is_valid_path(A, [(0, 0)], WORDS1)


def test_is_valid_path_row_board():
    assert not is_valid_path(C, [(1, 1)], WORDS2)
    assert is_valid_path(C, [(0, 0), (0, 1), (0, 2), (0, 3)], WORDS1) == "ABCD"
    # assert not is_valid_path(C, [], {"A": True})
    assert not is_valid_path(C, [(1, 0)], WORDS1)
    assert not is_valid_path(C, [(1, 1)], WORDS1)


def test_is_valid_path_col_board():
    assert not is_valid_path(E, [(1, 0)], WORDS2)
    assert is_valid_path(E, [(0, 0), (1, 0), (2, 0)],
                         {"AEAJR": True}) == "AEAJR"
    # assert not is_valid_path(E, [], {"A": True})
    assert not is_valid_path(E, [(1, 0)], WORDS1)
    assert not is_valid_path(E, [(1, 1)], WORDS1)


def test_find_length_n_words_4board():
    assert not find_length_n_words(4, B, {"a": True})
    assert not find_length_n_words(1, B, {"a": True})
    assert not find_length_n_words(1, B, {})
    assert not find_length_n_words(1, B, {"ABD": True})
    assert find_length_n_words(3, B, WORDS1) == B3WORDS1
    assert find_length_n_words(4, B, WORDS1) == B4WORDS1
    assert find_length_n_words(3, B, WORDS1) == B3WORDS1
    # assert find_length_n_words(1, B, WORDS1) == B1WORDS1
    assert find_length_n_words(9, B, WORDS1) == B9WORDS1


def test_find_length_n_words_5board():
    assert not find_length_n_words(4, D, {"a": True})
    assert not find_length_n_words(1, D, {"a": True})
    # assert find_length_n_words(1, D, {"A": True}) == [("A", [(0, 0)])]
    assert find_length_n_words(3, D, {"AEJ": True}) == [
        ("AEJ", [(0, 0), (1, 0), (2, 1)])]
    assert find_length_n_words(3, D, {"AEMJ": True}) == [
        ("AEMJ", [(4, 0), (3, 0), (2, 1)])]
    assert sorted(find_length_n_words(3, D, {"DHR": True})) == sorted([
        ("DHR", [(0, 3), (0, 4), (1, 4)]), ("DHR", [(0, 3), (1, 3), (1, 4)])])
    assert find_length_n_words(6, D, {"AETREWZRE/": True}) == [
        ("AETREWZRE/", [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4)])]

# def test_find_length_n_words_1board():
#     assert find_length_n_words(1, A, {"A": True}) == [("A", [(0, 0)])]
#     assert not find_length_n_words(2, A, {"A": True})
#     assert not find_length_n_words(1, A, {"B": True})

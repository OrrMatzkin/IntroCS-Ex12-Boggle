from ex12_utils import *

B = [["A", 'B', "C", "D"],
     ["E", "F", "G", "H"],
     ["I", "J", "K", "L"],
     ["M", "N", "O", "P"]]

WORDS1 = {"ABCD": True, "EFGK": True, "PON": True, "N": True, "ABCDHLPON":
    True}

LONG_COORD = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2),
              (3, 1)]


def test_is_valid_path():
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
    assert is_valid_path(B, [(3, 1)], WORDS1) == "N"
    assert is_valid_path(B, LONG_COORD, WORDS1) == "ABCDHLPON"
    assert not is_valid_path(B, [(0, 0), (2, 2)], {"AK": True})
    assert not is_valid_path(B, [(4, 0)], {"AK": True})
    assert not is_valid_path(B, [(0, 4)], {"AK": True})
    assert not is_valid_path(B, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 2)],
                             WORDS1)


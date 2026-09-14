import pytest

from assignment import (
    find_all_positions,
    find_student_by_id,
    binary_search_steps,
    find_insert_position,
    first_and_last_position,
)


class CountingList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.accesses = 0

    def __getitem__(self, index):
        self.accesses += 1
        return super().__getitem__(index)

    def __iter__(self):
        self.accesses += len(self)
        return super().__iter__()

    def __contains__(self, value):
        self.accesses += len(self)
        return super().__contains__(value)

    def index(self, *args):
        self.accesses += len(self)
        return super().index(*args)

    def count(self, value):
        self.accesses += len(self)
        return super().count(value)


@pytest.mark.parametrize(
    "data, target, expected",
    [
        ([4, 2, 4, 9, 4], 4, [0, 2, 4]),
        ([10, 20, 30], 20, [1]),
        ([10, 20, 30], 99, []),
        ([], 1, []),
        (["a", "b", "a", "c"], "a", [0, 2]),
        ([7, 7, 7, 7], 7, [0, 1, 2, 3]),
    ]
)
def test1(data, target, expected):
    assert find_all_positions(data, target) == expected

RECORDS = [
    (101, "Bat", 78),
    (205, "Saraa", 91),
    (144, "Tuguldur", 65),
    (317, "Anu", 88),
]


@pytest.mark.parametrize(
    "records, student_id, expected",
    [
        (RECORDS, 101, "Bat"),
        (RECORDS, 317, "Anu"),
        (RECORDS, 144, "Tuguldur"),
        (RECORDS, 999, None),
        ([], 101, None),
    ]
)
def test2(records, student_id, expected):
    assert find_student_by_id(records, student_id) == expected


@pytest.mark.parametrize(
    "data, target, expected",
    [
        ([1, 3, 5, 7, 9, 11, 13, 15], 7, (3, 1)),
        ([1, 3, 5, 7, 9, 11, 13, 15], 1, (0, 3)),
        ([1, 3, 5, 7, 9, 11, 13, 15], 15, (7, 4)),
        ([1, 3, 5, 7, 9, 11, 13, 15], 8, (-1, 3)),
        ([5], 5, (0, 1)),
        ([5], 2, (-1, 1)),
        ([], 5, (-1, 0)),
    ]
)
def test3(data, target, expected):
    assert binary_search_steps(data, target) == expected


@pytest.mark.parametrize(
    "data, value, expected",
    [
        ([10, 20, 30, 40], 25, 2),
        ([10, 20, 30, 40], 10, 0),
        ([10, 20, 30, 40], 40, 3),
        ([10, 20, 30, 40], 50, 4),
        ([10, 20, 30, 40], 5, 0),
        ([1, 2, 2, 2, 3], 2, 1),
        ([], 7, 0),
    ]
)
def test4(data, value, expected):
    assert find_insert_position(data, value) == expected


def test4_efficiency():
    data = CountingList(range(0, 200000, 2))
    assert find_insert_position(data, 123457) == 61729
    checked = data.accesses
    assert checked < 200, (
        "Too many elements checked (%d). Exercise 4 must use binary search."
        % checked
    )


@pytest.mark.parametrize(
    "data, target, expected",
    [
        ([1, 2, 2, 2, 3, 4], 2, (1, 3)),
        ([5, 5, 5, 5], 5, (0, 3)),
        ([1, 2, 3, 4], 4, (3, 3)),
        ([1, 2, 3, 4], 1, (0, 0)),
        ([1, 2, 3], 4, (-1, -1)),
        ([1, 3, 5], 4, (-1, -1)),
        ([], 1, (-1, -1)),
    ]
)
def test5(data, target, expected):
    assert first_and_last_position(data, target) == expected


def test5_efficiency():
    data = CountingList([1] * 50000 + [2] * 50000)
    assert first_and_last_position(data, 2) == (50000, 99999)
    checked = data.accesses
    assert checked < 200, (
        "Too many elements checked (%d). Exercise 5 must use binary search."
        % checked
    )

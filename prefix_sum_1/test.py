from algo import has_target_segment, make_prefix_sum


def test():
    assert make_prefix_sum([1, 2, 3]) == [0, 1, 3, 6]
    assert has_target_segment([1, 2, 3], 6) == (1, 3)
    assert has_target_segment([0, 0, 0], 2) == (-1, -1)
    assert make_prefix_sum([1, 5, 6]) == [0, 1, 6, 12]
    assert has_target_segment([1, 5, 6], 11) == (2, 3)
    assert has_target_segment([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == (1, 5)
    assert has_target_segment([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == (1, 3)
    assert has_target_segment([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19) == (9, 10)
    assert has_target_segment([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22) == (4, 7)

import pybind11_rdp as m


def test_main():
    assert m.rdp([[1, 1], [2, 2], [3, 3], [4, 4]]).shape == (2, 2)

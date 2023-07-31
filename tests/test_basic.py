import os
import sys
import time

import numpy as np
import pytest

from pybind11_rdp import LineSegment, rdp


def test_segment():
    seg = LineSegment([0, 0, 0], [10, 0, 0])
    assert 4.0 == seg.distance([5.0, 4.0, 0.0])
    assert 5.0 == seg.distance([-4.0, 3.0, 0.0])
    assert 5.0 == seg.distance([14.0, 3.0, 0.0])
    seg = LineSegment([0, 0, 0], [0, 0, 0])
    assert 5.0 == seg.distance([3.0, 4.0, 0.0])
    assert 5.0 == seg.distance([-4.0, 3.0, 0.0])
    assert 13.0 == seg.distance([5.0, 12.0, 0.0])


def test_rdp():
    assert rdp([[1, 1], [2, 2], [3, 3], [4, 4]], epsilon=1e-9).shape == (2, 2)
    assert rdp([[0, 0], [5, 1 + 1e-3], [10, 0]], epsilon=1).shape == (3, 2)
    assert rdp([[0, 0], [5, 1 - 1e-3], [10, 0]], epsilon=1).shape == (2, 2)


def test_degenerate_case():
    # https://github.com/mapbox/geojson-vt/issues/104
    coords = []
    for _ in range(14000):
        coords.extend(
            [
                [0.0, 0.0],
                [1.0, 0.0],
                [1.0, 1.0],
                [0.0, 1.0],
            ]
        )
    coords = np.array(coords)
    tick = time.time()
    ret = rdp(coords, 2e-15, algo="recursive")
    tock = time.time()
    print(tock - tick, "secs")  # 4 sec
    assert len(ret) == len(coords)


def pytest_main(dir: str, *, test_file: str = None):
    os.chdir(dir)
    sys.exit(
        pytest.main(
            [
                dir,
                *(["-k", test_file] if test_file else []),
                "--capture",
                "tee-sys",
                "-vv",
                "-x",
            ]
        )
    )


if __name__ == "__main__":
    pwd = os.path.abspath(os.path.dirname(__file__))
    pytest_main(pwd, test_file=os.path.basename(__file__))

import sys

import numpy as np
from _pybind11_rdp import LineSegment  # noqa
from _pybind11_rdp import __version__  # noqa
from _pybind11_rdp import rdp as _rdp  # noqa
from _pybind11_rdp import rdp_mask as _rdp_mask  # noqa


def __notify_dist_fn(dist):
    if dist is None:
        return
    print(
        "we don't support dist function, the only built-in dist function is dist(point,line_segment) (NOT dist(point,line))",
        file=sys.stderr,
    )


def rdp_rec(points, epsilon: float, dist=None):
    __notify_dist_fn(dist)
    points = np.asarray(points, dtype=np.float64)
    return _rdp(points, epsilon=epsilon, recursive=True)


def rdp_iter(points, epsilon: float, dist=None, return_mask=False):
    __notify_dist_fn(dist)
    points = np.asarray(points, dtype=np.float64)
    if return_mask:
        return _rdp_mask(points, epsilon=epsilon, recursive=False)
    return _rdp(points, epsilon=epsilon, recursive=False)


def rdp(points, epsilon: float = 0.0, dist=None, algo="iter", return_mask=False):
    __notify_dist_fn(dist)
    points = np.asarray(points, dtype=np.float64)
    recursive = "iter" != algo
    if return_mask:
        return _rdp_mask(points, epsilon=epsilon, recursive=recursive)
    return _rdp(points, epsilon=epsilon, recursive=recursive)

import sys

import numpy as np

from ._core import LineSegment  # noqa
from ._core import __version__  # noqa
from ._core import rdp_mask  # noqa
from ._core import rdp as _rdp  # noqa


def __notify_dist_fn(dist):
    """Internal function to notify users about dist function limitations.

    Args:
        dist: The distance function parameter (currently not supported)
    """
    if dist is None:
        return
    print(
        "we don't support dist function, the only built-in dist function is dist(point,line_segment) (NOT dist(point,line))",
        file=sys.stderr,
    )


def rdp_rec(points, epsilon: float, dist=None):
    """Recursive implementation of the Ramer-Douglas-Peucker algorithm.

    Args:
        points (array-like): Input points to be simplified. Will be converted to numpy array.
        epsilon (float): The maximum allowed distance between points and the simplified line.
        dist (callable, optional): Distance function (not supported, will be ignored).

    Returns:
        numpy.ndarray: Simplified points array.
    """
    __notify_dist_fn(dist)
    points = np.asarray(points, dtype=np.float64)
    return _rdp(points, epsilon=epsilon, recursive=True)


def rdp_iter(
    points,
    epsilon: float,
    dist=None,
    return_mask=False,
):
    """Iterative implementation of the Ramer-Douglas-Peucker algorithm.

    Args:
        points (array-like): Input points to be simplified. Will be converted to numpy array.
        epsilon (float): The maximum allowed distance between points and the simplified line.
        dist (callable, optional): Distance function (not supported, will be ignored).
        return_mask (bool, optional): If True, returns a boolean mask instead of simplified points.

    Returns:
        numpy.ndarray: If return_mask is False, returns simplified points array.
                      If return_mask is True, returns boolean mask indicating which points to keep.
    """
    __notify_dist_fn(dist)
    points = np.asarray(points, dtype=np.float64)
    if return_mask:
        return rdp_mask(points, epsilon=epsilon, recursive=False)
    return _rdp(points, epsilon=epsilon, recursive=False)


def rdp(
    points,
    epsilon: float = 0.0,
    dist=None,
    algo="iter",
    return_mask=False,
):
    """Main interface for the Ramer-Douglas-Peucker algorithm.

    Args:
        points (array-like): Input points to be simplified. Will be converted to numpy array.
        epsilon (float, optional): The maximum allowed distance between points and the simplified line.
                                 Defaults to 0.0.
        dist (callable, optional): Distance function (not supported, will be ignored).
        algo (str, optional): Algorithm to use, either "iter" (iterative) or "rec" (recursive).
                            Defaults to "iter".
        return_mask (bool, optional): If True, returns a boolean mask instead of simplified points.
                                    Defaults to False.

    Returns:
        numpy.ndarray: If return_mask is False, returns simplified points array.
                      If return_mask is True, returns boolean mask indicating which points to keep.
    """
    __notify_dist_fn(dist)
    points = np.asarray(points, dtype=np.float64)
    recursive = "iter" != algo
    if return_mask:
        return rdp_mask(points, epsilon=epsilon, recursive=recursive)
    return _rdp(points, epsilon=epsilon, recursive=recursive)

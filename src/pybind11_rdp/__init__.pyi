"""
C++/pybind11 version of Ramer-Douglas-Peucker (rdp) algorithm
-------------------------------------------------------------

.. currentmodule:: pybind11_rdp

.. autosummary::
   :toctree: _generate

   rdp
   rdp_mask
   LineSegment
"""

from __future__ import annotations

from typing import Any, overload

import numpy as np
from numpy.typing import NDArray

__doc__: str
__version__: str

class LineSegment:
    """
    A line segment defined by two points in 3D space.
    """

    def __init__(self, A: NDArray[np.float64], B: NDArray[np.float64]) -> None:
        """
        Create a new LineSegment.

        Args:
            A: First point of the line segment (3D coordinates)
            B: Second point of the line segment (3D coordinates)
        """
        ...
    def distance(self, P: NDArray[np.float64]) -> float:
        """
        Calculate the distance from a point to this line segment.

        Args:
            P: Point to calculate distance from (3D coordinates)

        Returns:
            float: Distance from point P to this line segment
        """
        ...
    def distance2(self, P: NDArray[np.float64]) -> float:
        """
        Calculate the squared distance from a point to this line segment.

        Args:
            P: Point to calculate distance from (3D coordinates)

        Returns:
            float: Squared distance from point P to this line segment
        """
        ...

@overload
def rdp(
    coords: NDArray[np.float64], *, epsilon: float = 0.0, recursive: bool = True
) -> NDArray[np.float64]:
    """
    Simplifies a given array of points using the Ramer-Douglas-Peucker algorithm.

    Args:
        coords: Array of points to simplify (Nx3 array)
        epsilon: Maximum allowed distance from the simplified line (default: 0.0)
        recursive: Whether to use recursive implementation (default: True)

    Returns:
        NDArray[np.float64]: Simplified array of points

    Example:
        >>> from pybind11_rdp import rdp
        >>> rdp([[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0]])
        array([[1, 1, 0], [4, 4, 0]])
    """
    ...

@overload
def rdp(
    coords: NDArray[np.float64], *, epsilon: float = 0.0, recursive: bool = True
) -> NDArray[np.float64]:
    """
    Simplifies a given array of points using the Ramer-Douglas-Peucker algorithm.

    Args:
        coords: Array of points to simplify (Nx2 array)
        epsilon: Maximum allowed distance from the simplified line (default: 0.0)
        recursive: Whether to use recursive implementation (default: True)

    Returns:
        NDArray[np.float64]: Simplified array of points

    Example:
        >>> from pybind11_rdp import rdp
        >>> rdp([[1, 1], [2, 2], [3, 3], [4, 4]])
        array([[1, 1], [4, 4]])
    """
    ...

@overload
def rdp_mask(
    coords: NDArray[np.float64], *, epsilon: float = 0.0, recursive: bool = True
) -> NDArray[np.int32]:
    """
    Returns a mask indicating which points to keep after simplification.

    Args:
        coords: Array of points to simplify (Nx3 array)
        epsilon: Maximum allowed distance from the simplified line (default: 0.0)
        recursive: Whether to use recursive implementation (default: True)

    Returns:
        NDArray[np.int32]: Boolean mask array where True indicates points to keep
    """
    ...

@overload
def rdp_mask(
    coords: NDArray[np.float64], *, epsilon: float = 0.0, recursive: bool = True
) -> NDArray[np.int32]:
    """
    Returns a mask indicating which points to keep after simplification.

    Args:
        coords: Array of points to simplify (Nx2 array)
        epsilon: Maximum allowed distance from the simplified line (default: 0.0)
        recursive: Whether to use recursive implementation (default: True)

    Returns:
        NDArray[np.int32]: Boolean mask array where True indicates points to keep
    """
    ...

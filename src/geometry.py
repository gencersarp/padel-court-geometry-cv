"""Utilities for estimating padel court geometry from monocular images.

This module intentionally starts small: it provides a compact representation
for a detected court quadrilateral and a helper to order four corner points in
clockwise screen-space order.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class CourtQuad:
    """Container for a 4-corner court quadrilateral in image coordinates."""

    corners: np.ndarray

    def as_array(self) -> np.ndarray:
        arr = np.asarray(self.corners, dtype=float)
        if arr.shape != (4, 2):
            raise ValueError("CourtQuad must contain shape (4, 2).")
        return arr


def order_quad_corners(points: Iterable[Iterable[float]]) -> np.ndarray:
    """Return four 2D points ordered clockwise starting from top-left.

    Parameters
    ----------
    points:
        Iterable containing exactly four 2D points.

    Returns
    -------
    np.ndarray
        Array of shape (4, 2) ordered as top-left, top-right,
        bottom-right, bottom-left.
    """

    pts = np.asarray(list(points), dtype=float)
    if pts.shape != (4, 2):
        raise ValueError("Expected exactly four 2D points.")

    sums = pts.sum(axis=1)
    diffs = np.diff(pts, axis=1).reshape(-1)

    top_left = pts[np.argmin(sums)]
    bottom_right = pts[np.argmax(sums)]
    top_right = pts[np.argmin(diffs)]
    bottom_left = pts[np.argmax(diffs)]

    return np.vstack([top_left, top_right, bottom_right, bottom_left])

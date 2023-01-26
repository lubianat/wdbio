# -*- coding: utf-8 -*-

"""Main code."""

from typing import List


def count(n: int) -> List[int]:
    """Count from 0 until n

    Args:
        n (int): Final number

    Returns:
        List[int]: A list of numbers from 0 until n
    """
    return list(range(0, n + 1))

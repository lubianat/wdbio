# -*- coding: utf-8 -*-

"""Trivial version test."""

import unittest

from wdbio import count


class TestCount(unittest.TestCase):
    """Trivially test counting"""

    def test_count(self):
        """Test counting.

        This is only meant to be an example test.
        """
        res = count(2)
        self.assertEqual(res, [0, 1, 2])

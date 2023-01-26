# -*- coding: utf-8 -*-

"""Trivial version test."""

import unittest

from wdbio.api import get_mitochondrial_genes


class TestApi(unittest.TestCase):
    def test_human(self):

        h = get_mitochondrial_genes("human")

        self.assertIn("MT-TV", h)
        self.assertGreater(len(h), 10)

    def test_mouse(self):

        m = get_mitochondrial_genes("mouse")

        self.assertIn("COX2", m)
        self.assertGreater(len(m), 10)

    def test_unexpected_species(self):
        with self.assertRaises(ValueError) as exc:
            get_mitochondrial_genes("wrong")
        self.assertEqual(str(exc.exception), "'species' can only be one of 'human' or 'mouse'")

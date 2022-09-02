""" Test the maximal repeats function. """

# pylint: disable=missing-docstring

import unittest

from parameterized import parameterized

from suffix_tree import Tree
from .tests import BUILDERS


class TestSupermaximalRepeats (unittest.TestCase):

    def supermaximal_repeats (self, tree, arr):
        a = []
        for cv, path in sorted (tree.supermaximal_repeats ()):
            a.append ("%d %s" % (cv, str (path)))
        self.assertEqual (a, arr)


    @parameterized.expand(BUILDERS)
    def test_supermaximal_repeats_1 (self, _, builder):
        # See [Gusfield1997]_ §7.12.1, 144ff.
        tree = Tree ({ 'A' : 'a1bx1ya1b' }, builder = builder)
        self.supermaximal_repeats (
            tree, [
                '1 a 1 b',
            ]
        )

    @parameterized.expand(BUILDERS)
    def test_supermaximal_repeats_2 (self, _, builder):
        tree = Tree ({
            'A' : '1abc2abc3',
            'B' : '4abc5abc6',
            'C' : '7abc',
            'D' : '7abc',
            'E' : 'abc',
        }, builder = builder)

        self.supermaximal_repeats (
            tree, [
                '2 7 a b c'
            ]
        )

if __name__ == '__main__':
    unittest.main ()
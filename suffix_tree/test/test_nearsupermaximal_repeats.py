""" Test the maximal repeats function. """

# pylint: disable=missing-docstring

import unittest

from parameterized import parameterized

from suffix_tree import Tree
from .tests import BUILDERS


class TestNearsupermaximalRepeats (unittest.TestCase):

    def nearsupermaximal_repeats (self, tree, arr):
        a = []
        for cv, path, score in sorted (tree.nearsupermaximal_repeats (score_decimals=2)):
            a.append ("%d %s %.2f" % (cv, str (path), score))
        self.assertEqual (a, arr)


    @parameterized.expand(BUILDERS)
    def test_nearsupermaximal_repeats_1 (self, _, builder):
        # See [Gusfield1997]_ §7.12.1, 144ff.
        tree = Tree ({ 'A' : 'a1bx1ya1b' }, builder = builder)
        self.nearsupermaximal_repeats (
            tree, [
                '1 1 0.33',
                '1 a 1 b 1.00'
            ]
        )

    @parameterized.expand(BUILDERS)
    def test_nearsupermaximal_repeats_2 (self, _, builder):
        tree = Tree ({
            'A' : '1abc2abc3',
            'B' : '4abc5abc6',
            'C' : '7abc',
            'D' : '7abc',
            'E' : 'abc',
        }, builder = builder)

        self.nearsupermaximal_repeats (
            tree, [
                '2 7 a b c 1.00',
                '5 a b c 0.71'
            ]
        )

if __name__ == '__main__':
    unittest.main ()
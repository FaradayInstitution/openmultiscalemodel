#
# Tests the _calculate module.
#
# This file is part of the Oxford RSE Python Template project.
#  Copyright (c) 2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the OxRSE
#  software package.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
import unittest
import oxrse


class AddSubtractTest(unittest.TestCase):
    """
    Tests the :meth:`add()` and :meth:`subtract()` methods.
    """
    def test_add(self):
        """
        Tests :meth:`oxrse.add()`.
        """
        self.assertEqual(oxrse.add(0, 0), 0)
        self.assertEqual(oxrse.add(0, 2), 2)
        self.assertEqual(oxrse.add(3, 0), 3)
        self.assertEqual(oxrse.add(4, 5), 9)
        self.assertEqual(oxrse.add(4, -5), -1)
        self.assertEqual(oxrse.add(-1, 1), 0)

    def test_subtract(self):
        """
        Tests :meth:`oxrse.add()`.
        """
        self.assertEqual(oxrse.subtract(0, 0), 0)
        self.assertEqual(oxrse.subtract(0, 2), -2)
        self.assertEqual(oxrse.subtract(3, 0), 3)
        self.assertEqual(oxrse.subtract(4, 5), -1)
        self.assertEqual(oxrse.subtract(4, -5), 9)
        self.assertEqual(oxrse.subtract(1, -1), 2)
        self.assertEqual(oxrse.subtract(-1, -1), 0)


#
# Tests the _float_rounder module.
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


class FloatRounderTest(unittest.TestCase):
    """
    Tests the :class:`FloatRounder` class.
    """
    def test_round_to_nearest(self):
        """
        Tests :meth:`FloatRounder.round()` in default mode (rounding to nearest
        integer).
        """
        r = oxrse.FloatRounder()

        # Test with positive numbers
        self.assertEqual(r.round(0), 0.0)
        self.assertEqual(r.round(0.4), 0.0)
        self.assertEqual(r.round(0.5), 0.0)
        self.assertEqual(r.round(0.5001), 1.0)
        self.assertEqual(r.round(0.9), 1.0)
        self.assertEqual(r.round(1.49), 1.0)
        self.assertEqual(r.round(1000.5), 1000.0)
        self.assertEqual(r.round(1000.5001), 1001.0)

        # Test with negative numbers
        self.assertEqual(r.round(-0), 0.0)
        self.assertEqual(r.round(-0.4), 0.0)
        self.assertEqual(r.round(-0.5), -0.0)
        self.assertEqual(r.round(-0.5001), -1.0)
        self.assertEqual(r.round(-0.9), -1.0)
        self.assertEqual(r.round(-1.49), -1.0)
        self.assertEqual(r.round(-1000.5), -1000.0)
        self.assertEqual(r.round(-1000.5001), -1001.0)

        # Test special values raise the appropriate exception
        self.assertRaisesRegexp(ValueError, "don't like", r.round, 1.23)

        # Test special values raise the appropriate exception
        self.assertRaisesRegexp(ValueError, 'worst number', r.round, 2.34)

    def test_round_towards_zero(self):
        """
        Tests :meth:`FloatRounder.round()` in round-towards-zero mode.
        """
        r = oxrse.FloatRounder(True)

        # Test with positive numbers
        self.assertEqual(r.round(0), 0.0)
        self.assertEqual(r.round(0.4), 0.0)
        self.assertEqual(r.round(0.5), 0.0)
        self.assertEqual(r.round(0.5001), 0.0)
        self.assertEqual(r.round(0.9), 0.0)
        self.assertEqual(r.round(1.49), 1.0)
        self.assertEqual(r.round(1000.5), 1000.0)
        self.assertEqual(r.round(1000.5001), 1000.0)

        # Test with negative numbers
        self.assertEqual(r.round(-0), 0.0)
        self.assertEqual(r.round(-0.4), 0.0)
        self.assertEqual(r.round(-0.5), 0.0)
        self.assertEqual(r.round(-0.5001), 0.0)
        self.assertEqual(r.round(-0.9), 0.0)
        self.assertEqual(r.round(-1.49), -1.0)
        self.assertEqual(r.round(-1000.5), -1000.0)
        self.assertEqual(r.round(-1000.5001), -1000.0)

        # Test special values raise the appropriate exception
        self.assertRaisesRegexp(ValueError, "don't like", r.round, 1.23)

        # Test special values raise the appropriate exception
        self.assertRaisesRegexp(ValueError, 'worst number', r.round, 2.34)

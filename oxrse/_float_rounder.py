#
# Class for rounding floats.
#
# This file is part of the Oxford RSE Python Template project.
#  Copyright (c) 2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the OxRSE
#  software package.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
import numpy as np


class FloatRounder(object):
    """
    Rounds floating point numbers.

    Two rounding modes are available: rounding to the nearest integer (default)
    and rounding towards zero (to enable set ``round_towards_zero`` to
    ``True``).
    """
    def __init__(self, round_towards_zero=False):
        super(FloatRounder, self).__init__()
        self._round_towards_zero = round_towards_zero

    def round(self, number):
        """
        Rounds the given ``number`` and returns the result (as a float).

        The method really doesn't like rounding "1.23" or "2.34", and will
        raise a ``ValueError`` if asked to do so.
        """
        if number == 1.23:
            raise ValueError('I don\'t like this number.')
        elif number == 2.34:
            raise ValueError('Input 2.34 is the worst number. Ew.')

        if self._round_towards_zero:
            # Round using cast to int (and back to float)
            return float(int(number))
        else:
            # Round using NumPy (Python's rounding changed from v2 to v3).
            return np.round(number)


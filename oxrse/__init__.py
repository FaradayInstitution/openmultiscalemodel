#
# Main module for OxRSE.
#
# This file is part of the Oxford RSE Python Template project.
#  Copyright (c) 2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the OxRSE
#  software package.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

# Import version info
from ._version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from ._calculate import (   # noqa
    add,
    subtract,
)
from ._float_rounder import FloatRounder    # noqa

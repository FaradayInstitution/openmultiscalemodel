#
# Version information fo OxRSE.
#
# See: https://packaging.python.org/guides/single-sourcing-package-version/
#
# This file is part of the Oxford RSE Python Template project.
#  Copyright (c) 2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the OxRSE
#  software package.
#

# Version as a tuple (major, minor, revision)
#  - Changes to major are rare
#  - Changes to minor indicate new features, possible slight backwards
#    incompatibility
#  - Changes to revision indicate bugfixes, tiny new features
VERSION_INT = 1, 0, 0

# String version of the version number
VERSION = '.'.join([str(x) for x in VERSION_INT])

#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2020, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from bokeh.core.has_props import HasProps

# Module under test
from bokeh.core.properties import Dict, Int, List, String # isort:skip

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

class _TestHasProps(HasProps):
    x = Int(12)
    y = String("hello")
    z = List(Int, [1, 2, 3])
    zz = Dict(String, Int)
    s = String(None)

class _TestModel(HasProps):
    x = Int(12)
    y = String("hello")
    z = List(Int, [1, 2, 3])
    zz = Dict(String, Int)
    s = String(None)

class _TestModel2(HasProps):
    x = Int(12)
    y = String("hello")
    z = List(Int, [1, 2, 3])
    zz = Dict(String, Int)
    s = String(None)

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

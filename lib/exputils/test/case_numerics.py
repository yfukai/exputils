# -*- coding:utf-8 -*-
# using konira

import os
import sys
import konira

LIB_DIR = os.path.realpath('../')

if not LIB_DIR in sys.path:
    sys.path.insert(0, LIB_DIR)
#
import exputils.numerics as numericsu

describe "numerics.interpolate_array":
    it "should interpolate circular array":
        r = numericsu.interpolate_array([1,2,-1,3],lambda x: x>0,True)
        assert r == [1,2,2.5,3]
        r = numericsu.interpolate_array([1,2,3,4,-1],lambda x: x>0,True)
        assert r == [1,2,3,4,2.5]
    it "should interpolate non circular array":
        r = numericsu.interpolate_array([1,2,-1,3],lambda x: x>0)
        assert r == [1,2,2.5,3]
        r = numericsu.interpolate_array([1,2,3,4,-1],lambda x: x>0)
        assert r == [1,2,3,4,4]

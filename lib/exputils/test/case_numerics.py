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

import math
describe "numerics.get_log_separated_array":
    it "should get appropreate array":
        result = numericsu.get_log_separated_array(10,1000,3)
        for i in range(len(result)):
            assert abs(result[i] - math.pow(10,1+i)) < 10e-5

import numpy as np
describe "numerics.fmod_positive":
    it "should apply appropreately":
        assert numericsu.fmod_positive(1.5,0.7) - 0.1 < 10e-7
        assert numericsu.fmod_positive(-1.4,0.4) - 0.2 < 10e-7

    it "should apply appropreately to array":
        result = numericsu.fmod_positive(np.array([1.5,-1.5]),0.7)
        assert result[0] - 0.1 < 10e-7
        assert result[1] - 0.6 < 10e-7


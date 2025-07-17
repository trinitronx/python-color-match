"""Monkey patch for numpy > 1.x to support deprecated asscalar function"""
import numpy

def patch_asscalar(a):
    return a.item()

setattr(numpy, "asscalar", patch_asscalar)

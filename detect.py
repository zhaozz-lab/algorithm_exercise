import sys
from ctypes import CDLL, POINTER, \
    c_int, c_void_p
import numpy as np


sim_dll = CDLL("./detector.dll")

detector_new_func = sim_dll.DetectorNew
detector_new_func.restype = c_void_p

detector_process_func = sim_dll.DetectorProcess
detector_process_func.argtypes = [c_void_p, POINTER(c_int), POINTER(c_int), c_int]

detector_delete_func = sim_dll.DetectorDelete
detector_delete_func.argtypes = [c_void_p]


class Detector():
    def __init__(self):
        self.obj = detector_new_func()

    def process(self, pin, pout, n):
        detector_process_func(self.obj, pin, pout, n)

    def __del__(self):
        detector_delete_func(self.obj)


def main():
    detector = Detector()

    n = 1024
    a = np.arange(n, dtype=np.uint32)
    b = np.zeros(n, dtype=np.int32)

    aptr = a.ctypes.data_as(POINTER(c_int))
    bptr = b.ctypes.data_as(POINTER(c_int))

    detector.process(aptr, bptr, n)


if __name__ == "__main__":
    print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
    main()

import numpy as np
class OrbitalElements():
    def __init__(self,
                 r = None,
                 v = None):
        self._vec_r = r
        self._vec_v = v
    def init_from_r_v(self):
        pass

    def init_from_orbital_elements(self):
        pass

    @property
    def vec_r(self):
        return  self._vec_v

    @property
    def vec_v(self):
        return  self._vec_r

    @property
    def vec_e(self):
        pass
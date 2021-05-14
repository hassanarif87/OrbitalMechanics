import numpy as np
import Constants

class ElipticalOrbit():
    def __init__(self,
                 planet,
                 momentum = None,
                 eccentricity = None,
                 parameter = None,
                 major_axis = None,
                 minor_axis = None):
        # Calcualte Specific energy and momentum of the orbit from whatever is avalible
        self.mu = Constants.G * Constants.mass_Earth
        self._h = momentum # Angular momentum of orbit
        self._e = eccentricity # Eccentricity
        self._p = parameter # Parameter
        self._c = major_axis # Minor Axis
        self._a = minor_axis # Major Axis

    @property
    def r_apoapsis(self):
        self.a * ( 1 + self.e)
    @property
    def r_periapsis(self):
        self.a * ( 1 - self.e)

    @property
    def h(self):
        # Orbital momentum
        if self._h:
            return self._h
        else:
           self._h = np.sqrt( self.mu * self.p)
           return self._h

    @property
    def specific_energy(self):
        return -1 * self.mu / ( 2  *self.a)

    @property
    def p(self):
        # Semilatus rectum (parameter)
        if self._p:
            return self._p
        else:
            self._p = self.h**2 / self.mu
            return self._p

    @property
    def e(self):
        # eccentricity
        if self._e:
            return self._e
        else:
            self._e = np.sqrt( 1 + ( 2 * self.specific_energy*self.h**2)/(self.mu**2))
            return self._e

    @property
    def a(self):
        if self._a:
            return self._a
        else:
            self._a = self.c / self .e
            return self._a

    @property
    def c(self):
        if self._c:
            return self._c
        else:
            self._c = self.a * self .e
            return self._c

    @property
    def period(self):
        return 2 * np.pi /np.sqrt(self.mu) * (self.a)**(3/2)
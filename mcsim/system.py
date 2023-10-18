import numpy as np


class System:
    """System object with the spin configuration and necessary parameters.

    Parameters
    ----------
    s: mcsim.Spins

        Two-dimensional spin field.

    B: Iterable

        External magnetic field, length 3.

    K: numbers.Real

        Uniaxial anisotropy constant.

    u: Iterable(float)

        Uniaxial anisotropy axis, length 3. If ``u`` is not normalised to 1, it
        will be normalised before the calculation of uniaxial anisotropy energy.

    J: numbers.Real

        Exchange energy constant.

    D: numbers.Real

        Dzyaloshinskii-Moriya energy constant.

    """

    def __init__(self, s, B, K, u, J, D):
        self.s = s
        self.J = J
        self.D = D
        self.B = B
        self.K = K
        self.u = u

    def energy(self):
        """Total energy of the system.

        The total energy of the system is computed as the sum of all individual
        energy terms.

        Returns
        -------
        float

            Total energy of the system.

        """
        return self.zeeman() + self.anisotropy() + self.exchange() + self.dmi()

    def zeeman(self):
        raise NotImplementedError

    def anisotropy(self):
        raise NotImplementedError

    def exchange(self):
        raise NotImplementedError

    def dmi(self):
        raise NotImplementedError

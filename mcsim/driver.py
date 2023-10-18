import numpy as np


def random_spin(s0, alpha=0.1):
    """Generate a new random spin based on the original one.

    Parameters
    ----------
    s0: np.ndarray

        The original spin that needs to be changed.

    alpha: float

        Larger alpha, larger the modification of the spin. Defaults to 0.1.

    Returns
    -------
    np.ndarray

        New updated spin, normalised to 1.

    """
    delta_s = (2 * np.random.random(3) - 1) * alpha
    s1 = s0 + delta_s
    return s1 / np.linalg.norm(s1)


class Driver:
    """Driver class.

    Driver class does not take any input parameters at initialisation.

    """

    def __init__(self):
        pass

    def drive(self, system, n, alpha=0.1):
        raise NotImplementedError

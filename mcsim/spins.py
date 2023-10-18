import numbers

import numpy as np


class Spins:
    """Field of spins on a two-dimensional lattice.

    Each spin is a three-dimensional vector s = (sx, sy, sz). Underlying data
    stucture (``self.array``) is a numpy array (``np.ndarray``) with shape
    ``(nx, ny, 3)``, where ``nx`` and ``ny`` are the number of spins in the x
    and y directions, respectively, and 3 to hold all three vector components of
    the spin.

    Parameters
    ----------
    n: Iterable

        Dimensions of a two-dimensional lattice ``n = (nx, ny)``, where ``nx``
        and ``ny`` are the number of atoms in x and y directions, respectively.
        Values of ``nx`` and ``ny`` must be positive integers.

    value: Iterable

        The value ``(sx, sy, sz)`` that is used to initialise all spins in the
        lattice. All elements of ``value`` must be real numbers. Defaults to
        ``(0, 0, 1)``.

    """

    def __init__(self, n, value=(0, 0, 1)):
        # Checks on input parameters.
        if len(n) != 2:
            raise ValueError(f"Length of iterable n must be 2, not {len(n)=}.")
        if any(i <= 0 or not isinstance(i, int) for i in n):
            raise ValueError("Elements of n must be positive integers.")

        if len(value) != 3:
            raise ValueError(f"Length of iterable value must be 3, not {len(n)=}.")
        if any(not isinstance(i, numbers.Real) for i in n):
            raise ValueError("Elements of value must be real numbers.")

        self.n = n
        self.array = np.empty((*self.n, 3), dtype=np.float64)
        self.array[..., :] = value

        if not np.isclose(value[0] ** 2 + value[1] ** 2 + value[2] ** 2, 1):
            # we ensure all spins' magnitudes are normalised to 1.
            self.normalise()

    @property
    def mean(self):
        raise NotImplementedError

    def __abs__(self):
        raise NotImplementedError

    def normalise(self):
        """Normalise the magnitude of all spins to 1."""
        self.array = self.array / abs(self)  # This computation will be failing until you implement __abs__.

    def randomise(self):
        """Initialise the lattice with random spins.

        Components of each spin are between -1 and 1: -1 <= si <= 1, and all
        spins are normalised to 1.

        """
        self.array = 2 * np.random.random((*self.n, 3)) - 1
        self.normalise()

    def plot(self):
        raise NotImplementedError

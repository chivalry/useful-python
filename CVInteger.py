class CVInteger(int):
    """Subclass of `int` that provides useful utility methods."""

    def is_prime(self):
        """Uses early prime facts to determine primacy more quickly.
        :return bool - `True` if self is a prime number, `False` otherwise
        :raises ValueError - If `self` is not a positive integer
        """
        if self <= 0:
            raise ValueError('Error: Only positive integers can be prime')
        if self in [2, 3, 5, 7]:
            return True
        if self < 2 or self % 2 == 0 or self == 9:
            return False
        if self % 3 == 0:
            return False
        root = int(self ** 0.5)
        fact = 5
        while fact <= root:
            if self % fact == 0 or self % (fact + 2) == 0:
                return False
            fact += 6
        return True

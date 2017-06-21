from gcd import gcd

class FloatingPoint8(object):
    bias = 7
    
    def __init__(self, s=0, exp=0, frac=0):
        self.set_s(s)
        self.set_exp(exp)
        self.set_frac(frac)

    def get_s(self):
        return self._s

    def get_exp(self):
        return self._exp

    def get_frac(self):
        return self._frac

    def set_s(self, s):
        assert s == 0 or s == 1, "s should be 0 or 1"
        self._s = s

    def set_exp(self, exp):
        assert exp >= 0 and exp < 16, "exp should be between 0 and 15 (inclusive)"
        self._exp = exp

    def set_frac(self, frac):
        assert frac >= 0 and frac < 8, "frac should be between 0 and 7 (inclusive)"
        self._frac = frac

    def __repr__(self):
        r = ""

        s = self.get_s()
        exp = self.get_exp()
        frac = self.get_frac()

        if exp == 15 and frac != 0:
            return "{}(NaN)".format(self.__class__.__name__)

        if exp == 15 and s == 0:
            return "{}(+Infinity)".format(self.__class__.__name__)

        if exp == 15 and s == 1:
            return "{}(-Infinity)".format(self.__class__.__name__)

        if exp == 0 and frac == 0:
            return "{}(0)".format(self.__class__.__name__)

        if exp == 0:
            E = 1 - self.bias
            numerator = frac
            denominator = 8 * (2 ** -E)
        else:
            E = exp - self.bias
            if E < 0:
                numerator = 8 + frac
                denominator = 8 * (2 ** -E)
            else:
                numerator = (8 + frac) * (2 ** E)
                denominator = 8

        d = gcd(numerator, denominator)
        numerator, denominator = numerator // d, denominator // d

        if denominator == 1:
            return "{}({})".format(self.__class__.__name__, ((-1) ** s) * numerator)
        else:
            return "{}({}/{})".format(self.__class__.__name__, ((-1) ** s) * numerator, denominator)

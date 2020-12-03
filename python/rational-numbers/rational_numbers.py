from __future__ import division
import math


class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        self.numer = int(numer/gcd)
        self.denom = int(denom/gcd)
        if self.denom < 0 :
            self.numer = -self.numer
            self.denom = -self.denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        num = self.numer*other.denom + self.denom*other.numer
        den = self.denom*other.denom
        return Rational(num,den)
        

    def __sub__(self, other):
        num = (self.numer*other.denom - self.denom*other.numer)
        den = self.denom * other.denom
        return Rational(num,den)

    def __mul__(self, other):
        num = self.numer * other.numer 
        den = self.denom * other.denom 
        return Rational(num,den)

    def __truediv__(self, other):
        num = self.numer * other.denom
        den = self.denom * other.numer 
        return Rational(num,den)

    def __abs__(self):
        num = ((self.numer)**2)**0.5
        den = ((self.denom)**2)**0.5
        return Rational(num,den)

    def __pow__(self, power):
        pass 

    def __rpow__(self, base):
        pass

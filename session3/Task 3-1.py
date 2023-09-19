import math


class ComplexOperations:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img < 0:
            return "{0:.2f}{1:.2f}i".format(self.real, self.img)
        else:
            return "{0:.2f}+{1:.2f}i".format(self.real, self.img)

    def __add__(self, other):
        # print("I'm in add function")
        real = self.real + other.real
        img = self.img + other.img
        return ComplexOperations(real, img)

    def __sub__(self, other):
        # print("I'm in sub function")
        real = self.real - other.real
        img = self.img - other.img
        return ComplexOperations(real, img)

    def __mul__(self, other):
        # print("im in mul function")
        real = (self.real * other.real) - (self.img * other.img)
        img = (self.real * other.img) + (self.img * other.real)
        return ComplexOperations(real, img)

    def __truediv__(self, other):
        # print("Im in div function")
        fraction = pow(other.real, 2) + pow(other.img, 2)
        real = (self.real * other.real + self.img * other.img) / fraction
        img = (self.img * other.real - self.real * other.img) / fraction
        return ComplexOperations(real, img)

    def mod(self):
        # print("I'M in mod function")
        return "{:.2f}".format(math.sqrt(pow(self.real, 2) + pow(self.img, 2)))


A = complex(input("1st number: "))  # use j
c = ComplexOperations(A.real, A.imag)
B = complex(input("2nd number: "))
d = ComplexOperations(B.real, B.imag)
print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(c.mod())
print(d.mod())

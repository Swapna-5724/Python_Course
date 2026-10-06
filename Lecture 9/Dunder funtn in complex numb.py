class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)      #Another Complex number is created and returned

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

# print(num1 + num2)      #  -> This occur error

num3 = num1.add(num2)     # Addition 2nd type
num3.showNumber()

num3 = num1 + num2        # Addition 1st type
num3.showNumber()

num3 = num1 - num2        # Subtraction
num3.showNumber()



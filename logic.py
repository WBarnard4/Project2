from PyQt6.QtWidgets import *
from gui import *
import random


# Logic when using the GUI
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Sets up GUI logic. Creates private variables. Creates button logic.
        """
        super().__init__()
        self.setupUi(self)

        self.__displayValue = '0'
        self.__mode = False

        # Button logic
        self.Button0.clicked.connect(lambda: self.numPad(0))
        self.Button1.clicked.connect(lambda: self.numPad(1))
        self.Button2.clicked.connect(lambda: self.numPad(2))
        self.Button3.clicked.connect(lambda: self.numPad(3))
        self.Button4.clicked.connect(lambda: self.numPad(4))
        self.Button5.clicked.connect(lambda: self.numPad(5))
        self.Button6.clicked.connect(lambda: self.numPad(6))
        self.Button7.clicked.connect(lambda: self.numPad(7))
        self.Button8.clicked.connect(lambda: self.numPad(8))
        self.Button9.clicked.connect(lambda: self.numPad(9))
        self.ButtonDec.clicked.connect(lambda: self.numPad('.'))
        self.openParButton.clicked.connect(lambda: self.numPad('('))
        self.closeParButton.clicked.connect(lambda: self.numPad(')'))

        self.delButton.clicked.connect(lambda: self.delete())
        self.clearButton.clicked.connect(lambda: self.clear())
        self.signButton.clicked.connect(lambda: self.signChange())

        self.squareButton.clicked.connect(lambda: self.powers(2))
        self.cubeButton.clicked.connect(lambda: self.powers(3))
        self.powerButton.clicked.connect(lambda: self.powers(None))
        self.sqrtButton.clicked.connect(lambda: self.roots(2))
        self.cbrtButton.clicked.connect(lambda: self.roots(3))
        self.rootButton.clicked.connect(lambda: self.roots(None))

        self.eButton.clicked.connect(lambda: self.e())
        self.piButton.clicked.connect(lambda: self.pi())
        self.randButton.clicked.connect(lambda: self.rand())

        self.modeButton.clicked.connect(lambda: self.mode())

        self.addButton.clicked.connect(lambda: self.add())
        self.subButton.clicked.connect(lambda: self.subtract())
        self.multButton.clicked.connect(lambda: self.multiply())
        self.divButton.clicked.connect(lambda: self.divide())
        self.equalButton.clicked.connect(lambda: self.equal())

    def numPad(self, num: int | str) -> None:
        """
        Handles adding numbers to the display based on input.
        :param num: The input to be displayed.
        """
        if num == 0 and self.__displayValue == '0':
            return
        if self.__displayValue == '0' and num != '.':
            self.__displayValue = ''
        elif self.__displayValue == '-0':
            self.__displayValue = '-'

        self.__displayValue += f'{num}'
        self.display()

    def delete(self) -> None:
        """
        Handles deleting the last character in the display.
        """
        self.__displayValue = self.__displayValue[:-1]
        if self.__displayValue == '' or self.__displayValue == '-':
            self.__displayValue = '0'
        self.display()

    def clear(self) -> None:
        """
        Handles completely clearing the display.
        """
        self.__displayValue = '0'
        self.display()

    def signChange(self) -> None:
        """
        Handles changing the sign of the display.
        """
        if self.__displayValue[0] != '-':
            self.__displayValue = '-' + self.__displayValue
        else:
            self.__displayValue = self.__displayValue[1:]
        self.display()

    def add(self) -> None:
        """
        Handles adding a + to the display.
        """
        self.__displayValue += '+'
        self.display()

    def subtract(self) -> None:
        """
        Handles adding a - to the display.
        """
        self.__displayValue += '-'
        self.display()

    def multiply(self) -> None:
        """
        Handles adding a * to the display.
        """
        self.__displayValue += '*'
        self.display()

    def divide(self) -> None:
        """
        Handles adding a / to the display.
        """
        self.__displayValue += '/'
        self.display()

    def equal(self) -> None:
        """
        Handles calculating the equation in the display.
        Has exception handling for equations with errors.
        """
        try:
            x = eval(f'{self.__displayValue}')
            self.__displayValue = f'{round(x, 8)}'
            self.display()
        except ZeroDivisionError:
            self.__displayValue = '0'
            self.numDisplay.setText('Divide by Zero')
        except SyntaxError:
            self.__displayValue = '0'
            self.numDisplay.setText('Syntax Error')
        except TypeError:
            self.__displayValue = '0'
            self.numDisplay.setText('Type Error')

    def powers(self, power: int | None) -> None:
        """
        Handles raising the display value to a power.
        If the power is not 2 or 3, it adds f'**' to the display.
        :param power: The power to raise to.
        """
        if power:
            self.__displayValue += f'**{power}'
            self.equal()
        else:
            self.__displayValue += f'**'
        self.display()

    def roots(self, root: int | None) -> None:
        """
        Handles taking the root of the display value.
        If the root is not 2 or 3, it adds f'**1(/' to the display.
        :param root: The root to take the display value to.
        """
        if root:
            self.__displayValue += f'**(1/{root})'
            self.equal()
        else:
            self.__displayValue += f'**(1/'
        self.display()

    def e(self) -> None:
        """
        Handles adding the value of e to the display
        """
        self.__displayValue += '2.71828'
        self.display()

    def pi(self) -> None:
        """
        Handles adding the value of pi to the display
        """
        self.__displayValue += '3.14159'
        self.display()

    def rand(self) -> None:
        """
        Creates a random number from 0 to 1 and adds it to the display.
        """
        randNum = round(random.random(), 8)
        if self.__displayValue == '0':
            self.__displayValue = ''
        self.__displayValue += f'{randNum}'
        self.display()

    def mode(self) -> None:
        """
        Handles changing the mode, which changes the window size,
        revealing additional functions
        """
        self.__mode = not self.__mode

        if self.__mode:
            self.setMaximumWidth(520)
            self.setMinimumWidth(520)
        else:
            self.setMinimumWidth(300)
            self.setMaximumWidth(300)

    def display(self) -> None:
        """
        Handles updating the display with the appropriate value.
        """
        self.numDisplay.setText(self.__displayValue)

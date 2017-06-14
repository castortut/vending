import time

from states import *


class Vending:

    lcd = None
    reader = None
    keypad = None

    timeout = 0
    state = IDLE
    selection = None

    def __init__(self, test=False):
        logging.getLogger().setLevel(logging.INFO)
        logging.info("Starting")

        if not test:
            from LCD import LCD
            from Reader import Reader
            from Keypad import Keypad

            self.lcd = LCD()
            self.reader = Reader()
            self.keypad = Keypad()
        else:
            from testLCD import TestLCD
            from testReader import TestReader
            from testKeypad import TestKeypad

            self.lcd = TestLCD()
            self.reader = TestReader()
            self.keypad = TestKeypad()

    def main(self):
        # Initialize state
        goto_idle(self)

        logging.info("Initialized")

        while True:
            btn = self.keypad.read()
            packet = self.reader.get_packet()

            if self.state == IDLE:
                state_idle(self, btn, packet)

            if self.state == PRODUCT_CHOSEN:
                state_product_chosen(self, btn, packet)

            if self.state == DISPLAY_TRANS:
                state_display_trans(self, btn, packet)

            if self.state == DISPLAY_ACC:
                state_display_acc(self, btn, packet)

            time.sleep(0.01)
            if self.timeout > 0:
                self.timeout -= 1


if __name__ == '__main__':
    app = Vending()
    app.main()

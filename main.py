import logging
import time

from LCD import LCD
from Reader import Reader
from Keypad import Keypad

from states import *


class Vending:

    lcd = None
    reader = None
    keypad = None

    # States
    IDLE = 0
    PRODUCT_CHOSEN = 1
    PRODUCT_CHOSEN_TIMEOUT = 200
    DISPLAY_TRANS = 2
    DISPLAY_TRANS_TIMEOUT = 200
    DISPLAY_ACC = 3
    DISPLAY_ACC_TIMEOUT = 200

    timeout = 0
    state = IDLE
    selection = None

    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)
        logging.info("Starting")

        self.lcd = LCD()
        self.reader = Reader()
        self.keypad = Keypad()

    def main(self):
        self.lcd.print(0, "Kassakone")
        logging.info("Initialized")
        while True:
            btn = self.keypad.read()
            packet = self.reader.get_packet()

            if self.state == self.IDLE:
                state_idle(self, btn, packet)

            if self.state == self.PRODUCT_CHOSEN:
                state_product_chosen(self, btn, packet)

            if self.state == self.DISPLAY_TRANS:
                state_display_trans(self, btn, packet)

            if self.state == self.DISPLAY_ACC:
                state_display_acc(self, btn, packet)

            time.sleep(0.01)
            if self.timeout > 0:
                self.timeout -= 1


if __name__ == '__main__':
    app = Vending()
    app.main()

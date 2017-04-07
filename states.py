import logging

from tmp_products import products

# States
IDLE = 0
PRODUCT_CHOSEN = 1
PRODUCT_CHOSEN_TIMEOUT = 200
DISPLAY_TRANS = 2
DISPLAY_TRANS_TIMEOUT = 200
DISPLAY_ACC = 3
DISPLAY_ACC_TIMEOUT = 200


def goto_display_transaction(packet, self):
    self.lcd.clear_rows((1, 2, 3))
    self.lcd.print(2, "Kortti: " + packet[:4])
    self.lcd.print(3, "Jaljella: X e")
    logging.info("Transaction complete")
    self.state = DISPLAY_TRANS
    self.timeout = DISPLAY_TRANS_TIMEOUT


def state_display_trans(self, btn, packet):
    if self.timeout == 0:
        goto_idle(self)


def goto_display_account(packet, self):
    self.lcd.clear_rows((1, 2, 3))
    self.lcd.print(2, "Kortti: " + packet[:4])
    self.lcd.print(3, "Saldo: X e")
    self.state = DISPLAY_ACC
    self.timeout = DISPLAY_ACC_TIMEOUT
    logging.info("Displaying account")


def state_display_acc(self, btn, packet):
    if self.timeout == 0:
        goto_idle(self)


def goto_product_chosen(btn, self):
    self.lcd.clear_rows((1, 2, 3))
    self.selection = btn - 1
    try:
        logging.info("Product chosen")
        self.lcd.print(1, "Tuote " + products[self.selection][0])
        self.lcd.print(2, "Hinta: " + str(products[btn - 1][1]))
        self.lcd.print(3, "Nayta kortti")
    except IndexError:
        logging.info("Invalid product chosen")
        self.lcd.clear_row(2)
        self.lcd.print(2, "Ei tuotetta")
    self.state = PRODUCT_CHOSEN
    self.timeout = PRODUCT_CHOSEN_TIMEOUT


def state_product_chosen(self, btn, packet):
    if btn and btn != (self.selection + 1):
        goto_product_chosen(btn, self)
    elif packet:
        goto_display_transaction(packet, self)
    elif self.timeout == 0:
        goto_idle(self)


def goto_idle(self):
    self.lcd.clear_rows((1, 2, 3))
    self.lcd.print(2, "Valitse tuote")
    self.state = IDLE


def state_idle(self, btn, packet):
    if btn:
        goto_product_chosen(btn, self)
    elif packet:
        goto_display_account(packet, self)
        pass
    else:
        pass


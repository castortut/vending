from RPLCD import CharLCD


class LCD:

    lcd = None

    def __init__(self):
        self.lcd = CharLCD()

    def print(self, row, message):
        self.lcd.cursor_pos = (row, 0)
        self.lcd.write_string(message)

    def clear_row(self, row):
        self.print(row, "                    ")

    def clear_rows(self, rows):
        for row in rows:
            self.clear_row(row)

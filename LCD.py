from RPLCD import CharLCD


class LCD:

    lcd = None

    def __init__(self):
        self.lcd = CharLCD()

    def print(self, row, message):
        """
        Writes a message to the given row
        :param row: Row number to print on (0-3)
        :param message: Message to print. If over 20 characters it wraps to the next line
        """
        self.lcd.cursor_pos = (row, 0)
        self.lcd.write_string(message)

    def clear_row(self, row):
        """
        Clear a single row
        :param row: Row number to clear (0-3)
        """
        self.print(row, "                    ")

    def clear_rows(self, rows):
        """
        Clear multiple rows
        :param rows: List of rows to clear 
        """
        for row in rows:
            self.clear_row(row)

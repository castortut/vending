class TestLCD:
    """
    A mock of the LCD class for testing without hardware
    """

    buf = ["", "", "", ""]

    def __init__(self):
        pass

    def print(self, row, message):
        """
        Writes a message to the given row
        :param row: Row number to print on (0-3)
        :param message: Message to print. If over 20 characters it wraps to the next line
        """
        self.buf[row] = message
        self.update()

    def clear_row(self, row):
        """
        Clear a single row
        :param row: Row number to clear (0-3)
        """
        self.buf[row] = ""
        self.update()

    def clear_rows(self, rows):
        """
        Clear multiple rows
        :param rows: List of rows to clear 
        """
        for row in rows:
            self.clear_row(row)

    def update(self):
        print("\n" * 10)
        for row in self.buf:
            print(row)

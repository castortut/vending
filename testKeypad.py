class TestKeypad:
    """
    A mock of the Keypad class for testing without hardware 
    """

    def __init__(self):
        pass

    def read(self):
        """
        Check if buttons are pressed
        :return: Number of first button being pressed (1-4), None if none are pressed
        """
        return 1

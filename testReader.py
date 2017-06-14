import random


class TestReader:
    """
    A mock of the Reader class for testing without hardware
    """

    tokens = ["ABCDEFGH12345678", "1234567812345678", "ABCDEFGHIJKLMNOP"]

    def __init__(self, port=None):
        pass

    def get_packet(self):
        """
        Receive a full packet from the reader
        :return: token serial number (16 characters) 
        """
        token = random.choice(self.tokens)
        return token

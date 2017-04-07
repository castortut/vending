import serial
import time


class Reader:

    DEFAULT_PORT = "/dev/ttyUSB0"

    port = None

    def __init__(self, port=None):
        if port is None:
            port = self.DEFAULT_PORT

        self.open_port(port)

    def open_port(self, port):
        """
        Open the serial port for the reader
        :param port: Serial port address, e.g. /dev/ttyUSB0 or COM1
        """
        self.port = serial.Serial(port, 9600, timeout=0, parity=serial.PARITY_NONE)

    def get_packet(self):
        """
        Receive a full packet from the reader
        :return: token serial number (16 characters) 
        """
        while True:
            packet = ""
            while True:
                data = self.port.read(100)
                if len(data):
                    packet += data.decode("ASCII")
                    time.sleep(0.1)
                else:
                    if len(packet):
                        print(packet.strip())
                        return packet.strip()[1:17]
                    else:
                        return None

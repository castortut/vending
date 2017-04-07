import RPi.GPIO as GPIO


class Keypad:

    switches = [7, 11, 13, 19]

    def __init__(self):
        for sw in self.switches:
            GPIO.setup(sw, GPIO.IN)

    def read(self):
        """
        Check if buttons are pressed
        :return: Number of first button being pressed (1-4), None if none are pressed
        """
        for sw in self.switches:
            if GPIO.input(sw):
                return self.switches.index(sw) + 1

        return None

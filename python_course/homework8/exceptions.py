class ZeroDivision(Exception):
    def __init__(self, text):
        self.txt = text


class NotDigit(ValueError):
    def __init__(self, value):
        self.value = value
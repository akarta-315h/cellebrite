"""
from Mits.Utils.upy import upy

#from serial           import PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE
class ConnectionSerial(IConnection):
        self.serial.set_timeout(timeout)
        if to_open_connection == True:

    def __repr__(self):

    def __to_upy_parity(self, par):

    def get_port(self):

    def set_port(self, port):

    def connect(self):

    def close(self):

    def send(self, data):

    def recv(self, num_bytes = 1024):

    def get_timeout(self):

    def set_timeout(self, timeout): # sec

    def set_baudrate(self, baud):

    def set_parity(self, par):

    def set_rts(self, n):

    def set_dtr(self, n):

    def set_byte_size(self, n):
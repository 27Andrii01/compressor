"""
This module make Deflate algorithm
"""
from lz77 import LZ77
from huffman import HuffmanCode

class Deflate_Algorithm(LZ77,HuffmanCode):
    """
    Class make deflate algorithm
    """
    def __init__(self, bufer_size) -> None:
        """
        The constructor of a class.
        """
        LZ77.__init__(self, buffer_size)
        HuffmanCode.__init__(self)

    def encode(self, text):
        """
        Method make encoding.
        """
        return HuffmanCode.encode([tuple(elem) for elem in LZ77(self.buffer_size).encode(text)])

    def decode(self, encoded_list, dct) -> str:
        """
        Method decode encoding info
        """
        decoded_by_huff = HuffmanCode.decode(encoded_list, dct)
        return LZ77(self.buffer_size).decode(HuffmanCode.decode(encoded_list, dct))

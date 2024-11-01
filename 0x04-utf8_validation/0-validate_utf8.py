#!/usr/bin/python3
"""Module: 0-validate_utf8"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding
    :returns: True if data is valid otherwise False
    """
    i, j = 0, 0
    data_len = len(data)
    while i < data_len:
        if (data[i] & 0b11100000) == 0b11000000:
            j = 1
        if (data[i] & 0b11110000) == 0b11100000:
            j = 2
        if (data[i] & 0b11111000) == 0b11110000:
            j = 3
        if (data[i] & 0b11000000) == 0b10000000:
            return False
        i += 1
        for _ in range(j):
            if (i >= data_len and j) or (data[i] & 0b11000000) != 0b10000000:
                return False
            i += 1
        j = 0
    return True

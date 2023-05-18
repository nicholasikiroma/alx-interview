#!/usr/bin/python3
"""Module for ALX Interview Task"""


def validUTF8(data):
    """
    Return: True if data is a
    valid UTF-8 encoding,
    else return False
    """
    num_bytes = 0

    for i, byte in enumerate(data):
        if num_bytes == 0:
            # If the current byte is a single byte character (ASCII character)
            if (byte >> 7) == 0:
                continue
            # Count the number of leading 1s to determine the number of bytes in the UTF-8 character
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # If the current byte is not a continuation byte, it's invalid
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If all bytes have been consumed and no incomplete character remains
    return True

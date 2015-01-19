#!/usr/bin/python
"""
The hexdump utility is a filter which displays the data input in hexadecimal
format.
"""
import binascii

__all__ = ['hexdump']

def dump(binary, size=4):
    """dump binary data in chunks of 2 octets."""
    hexstr = binascii.hexlify(binary)
    return ' '.join(genchunks(hexstr, size))

def genchunks(seq, size):
    """yield chunks of size from seq"""
    quotient, rest = divmod(len(seq), size)
    for i in range(quotient):
        yield seq[i*size:(i+1)*size]
    if rest:
        yield seq[quotient*size:]

def genhex(data):
    """yield lines in hex format including address info and printable chars."""
    line = ''
    generator = genchunks(data, 16)
    for addr, dat in enumerate(generator):
        line = '0x%04X: ' % (addr*16)
        line += dump(dat)
        # add padding
        pad = 2
        if len(dat) < 16:
            rest = 16-len(dat)
            pad += 2*rest + rest/2
        line += ' '*pad

        for byte in dat:
            byte = ord(byte)
            if 0x20 <= byte <= 0x7E:
                line += chr(byte)
            else:
                line += '.'

        yield line

def hexdump(data, result='print'):
    """
    Dump data in hexadecimal format: either printing to standard output or
    yielding a generator.

    @param data: data to dump in hexadecimal format.
    @type data: C{string}.
    @param result: how to yield the result: 'print' (default) or 'generator'.
    @type result: C{string}.
    @return: generator yielding lines of data in hex format
             (if result requires this).
    @rtype: C{generator} or None.
    @raise ValueError: when value of 'result' argument is unknown.
    """
    gen = genhex(data)
    if result == 'print':
        for line in gen:
            print line
    elif result == 'generator':
        return gen
    else:
        raise ValueError("Unknown value of 'result' argument")


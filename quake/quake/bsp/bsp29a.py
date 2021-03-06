"""This module provides file I/O for Quake BSP2 map files.

Example:
    bsp_file = bsp.Bsp.open('ad_sepulcher.bsp')
"""

import struct

from .bsp29 import Bsp as Bsp29


__all__ = ['is_bspfile', 'Bsp']


def _check_bspfile(fp):
    fp.seek(0)
    data = fp.read(struct.calcsize('<4s'))
    version = struct.unpack('<4s', data)[0]

    return version == b'BSP2'


def is_bspfile(filename):
    """Quickly see if a file is a bsp file by checking the magic number.

    The filename argument may be a file for file-like object.
    """
    try:
        if hasattr(filename, 'read'):
            return _check_bspfile(fp=filename)
        else:
            with open(filename, 'rb') as fp:
                return _check_bspfile(fp)
    except:
        pass

    return False


class Node(Bsp29.Node):
    format = '<i8i2I'
    size = struct.calcsize(format)


class Face(Bsp29.Face):
    format = '<2ii2i4Bi'
    size = struct.calcsize(format)


class ClipNode(Bsp29.ClipNode):
    format = '<i2i'
    size = struct.calcsize(format)


class Leaf(Bsp29.Leaf):
    format = '<2i6i2I4B'
    size = struct.calcsize(format)


class Edge(Bsp29.Edge):
    format = '<2I'
    size = struct.calcsize(format)


class Bsp(Bsp29):
    Node = Node
    Face = Face
    ClipNode = ClipNode
    Leaf = Leaf
    Edge = Edge

Bsp.Bsp = Bsp

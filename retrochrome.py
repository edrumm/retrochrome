#!/usr/bin/python

from gimpfu import *


def retrochrome(image, drawable, args):
    return


register(
    "Retrochrome",
    "Adds retro chrome fill effects to shapes",
    "For help, see: github.com/edrumm/retrochrome",
    "edrumm",
    "edrumm",
    "2023",
    "<Image>/Filters/Render/Retrochrome...",
    "*",
    [
        (PF_STRING, "args", "Input args", "default")
    ],
    [],
    retrochrome)
main()


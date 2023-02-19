#!/usr/bin/python

from gimpfu import *
import gimpcolor
import traceback


WHITE = gimpcolor.RGB(255, 255, 255, 255)
BLACK = gimpcolor.RGB(0, 0, 0, 255)


def get_active_drawable(image):
    return pdb.gimp_image_get_active_drawable(image)


def retrochrome(image, drawable, burn):
    # TODO prefix with image_ ?
    height = pdb.gimp_image_height(image)
    width = pdb.gimp_image_width(image)

    rc_layer_temp = pdb.gimp_layer_new(image, width, height, 0, "retrochrome-temp", 100, 0)

    # TODO determine layer position, temp value for now
    rc_layer_temp_pos = 1
    
    # TODO check None is correct for parent, should be
    pdb.gimp_image_insert_layer(image, rc_layer_temp, None, rc_layer_temp_pos)
    rc_temp_layer = pdb.gimp_image_merge_down(image, drawable, 0)

    drawable = get_active_drawable(image)
    pdb.plug_in_gauss(image, drawable, 5, 5, 0)

    pdb.gimp_image_select_color(image, 0, drawable, BLACK)
    pdb.gimp_selection_invert(image)

    return


# error handling
# try:
#   ...
# except Exception as e:
#   pdb_gimp_message(traceback.format_exc())

register(
    "Retrochrome",
    "Fill the current selection with a chrome effect",
    "For help, see: github.com/edrumm/retrochrome",
    "edrumm",
    "Ewan Drummond",
    "2023",
    "<Image>/Filters/Render/Retrochrome...",
    "*",
    [
        (PF_BOOL, "burn", "Apply burn?", 0)
    ],
    [],
    retrochrome)
main()


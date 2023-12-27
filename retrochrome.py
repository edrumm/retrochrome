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
    height = image.height
    width = image.width

    rc_layer_temp = pdb.gimp_layer_new(image, width, height, RGB_IMAGE, "retrochrome-temp", 100, LAYER_MODE_NORMAL_LEGACY)
    rc_layer_temp_pos = 0  # pdb.gimp_image_get_item_position(image, rc_layer_temp)
    
    # TODO check None is correct for parent, should be
    # TODO check why this merges into background. Reproduce with layers: Background, text layer to apply effect, arbitrary layer above
    pdb.gimp_image_insert_layer(image, rc_layer_temp, None, 1)
    rc_temp_layer = pdb.gimp_image_merge_down(image, drawable, EXPAND_AS_NECESSARY)

    drawable = get_active_drawable(image)

    pdb.plug_in_gauss_rle(image, drawable, 5, 1, 1)

    pdb.gimp_image_select_color(image, CHANNEL_OP_ADD, drawable, BLACK)
    pdb.gimp_selection_invert(image)
    pdb.gimp_layer_set_visible(rc_temp_layer, 0)

    # Work in progress
    # rc_chrome_layer = pdb.gimp_layer_new(image, width, height, RGB_IMAGE, "retrochrome-chrome", 100, LAYER_MODE_NORMAL_LEGACY)
    # pdb.gimp_image_insert_layer(image, rc_chrome_layer, None, rc_layer_temp_pos + 1)

    # drawable = get_active_drawable(image)

    rc_gradient = pdb.gimp_gradient_new("rc_gradient")
    # TODO add colour list
    rc_gradient_colours = [
        WHITE,
        BLACK
    ]

    # Work in progress
    # TODO set segments according to rc_gradient colours, 0 for now
    # pdb.gimp_gradient_segment_set_left_color(rc_gradient, 0, WHITE, 100)
    # pdb.gimp_gradient_segment_set_right_color(rc_gradient, 0, BLACK, 100)
    # pdb.gimp_context_set_gradient(rc_gradient)
    # TODO set supersampling and gradient coordinates
    # pdb.gimp_drawable_edit_gradient_fill(drawable, GRADIENT_LINEAR, 0, 0, 1, 1, 1, 0, 0, width // 2, height)


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


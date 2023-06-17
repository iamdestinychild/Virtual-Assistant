
import os
import winshell
import shutil
import tempfile


def clear_bin():
    recycle_bin = winshell.recycle_bin()

    items_list = list(recycle_bin)
    num_items = len(items_list)


    message = ''

    if num_items == 0:
        message = "Bin Is Already Empty"
        return message
    elif num_items >= 1:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        message = "Clear Recircle Bin Succesful"
        return message
    else:
        message = "Error Occured"
        return message


def bin_count():
    recycle_bin = winshell.recycle_bin()
    item_count = 0

    for item in recycle_bin:
        item_count += 1

    return item_count

    item_count = count_items_in_recycle_bin()
    return item_count




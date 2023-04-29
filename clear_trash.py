
import os
import winshell
import shutil
import tempfile


def clear_bin():
    recycle_bin = winshell.recycle_bin()

    items_list = list(recycle_bin)
    num_items = len(items_list)


    if num_items == 0:
        return print('bin is already empty')
    elif num_items >= 1:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        return print('Success')
    else:
        return("error occured")

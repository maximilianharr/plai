#!/usr/bin/env python
# -*- coding: utf-8 -*-

## @package workspace.init
# @brief Function collection for workspace initialization
# @author Maximilian Harr <maximilian.harr@gmail.com>
# @date 30.04.2020
#
# @bug
# @todo 
#

# IMPORTS ###########################################################
import os
import sys


# FUNCTIONS #########################################################
## @brief Appends workspace directory so that RD-UAM libraries can be loaded
# @return None
def load_workspace():
    try:
        ws_path = get_ws_path()
    except ValueError:
        return False
    sys.path.append(ws_path)
    return True

## @brief Searches folder containing src and README.md
# @return path is the workspace path with trailing slash or backslash
def get_ws_path():
    path = os.path.dirname(os.path.realpath(__file__))
    found_ws = False

    # Go back in directory until src and README.md found
    while found_ws is False:
        dir = os.listdir(path)
        if '__root__.py' in dir:
            found_ws = True
            break
        if len(dir) is 0:
            raise ValueError("Unable to locate workspace directory. Please execute script anywhere in your workspace.")
        else: # Remove one folder
            id = path.rfind("/")  # Linux
            if id != -1:
                path = path[0:id]
            id = path.rfind("\\")  # Windows
            if id != -1:
                path = path[0:id]

    # Append trailing slash if not present (independent of Linux / Windows
    path = os.path.join(path, '')

    return path

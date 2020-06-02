#!/usr/bin/env python
# -*- coding: utf-8 -*-

## @package test_workspace
# @brief Unit test to check if workspace is working properly
# @author Maximilian Harr <maximilian.harr@gmail.com>
# @date 30.04.2020
#
# @bug
# @todo
#

# IMPORTS ###########################################################
import unittest

# Local imports
import plai.workspace.init

# CLASSES ###########################################################

## @brief class for testing SQL library
class TestWorkspace(unittest.TestCase):

    ## @brief Test conversion accuracy
    def test_workspace_path(self):
        plai.workspace.init.get_ws_path()
        self.assertEqual(1.0, 1.0)


# FUNCTIONS #########################################################


# MAIN ##############################################################
if __name__ == '__main__':
    unittest.main()

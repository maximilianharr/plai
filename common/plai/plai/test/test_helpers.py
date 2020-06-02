"""@package text

  @brief Helper functions for Kaggle Global-Wheat-Detection competition
    https://www.kaggle.com/c/global-wheat-detection/overview
  
  @author Maximilian Harr <maximilian.harr@gmail.com>
  @date 29.05.2020

  @bug
  @warning
  @todo
 
"""

# IMPORTS ########################################################################################
import unittest
import math
from pyquaternion import Quaternion as pyquat
import numpy as np

# Local imports
import wheat_helpers

# CLASSES ########################################################################################

class TestData(unittest.TestCase):

    def test_transformation_matrix(self):
        array = wheat_helpers.get_array_from_string("[1.2, 2.3, 3.4]")
        
        self.assertEqual( array[0], 1.2 )
        self.assertEqual( array[1], 2.3 )
        self.assertEqual( array[2], 3.4 )

# FUNCTIONS ######################################################################################


# MAIN ###########################################################################################
if __name__ == '__main__':
    unittest.main()

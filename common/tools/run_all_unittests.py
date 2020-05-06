#!/usr/bin/env python
# -*- coding: utf-8 -*-

## @package test
# @brief Iteratively searches all unittest "*/test/test_*.py" and runs them
# @author Maximilian Harr <maximilian.harr@gmail.com>
# @date 30.04.2020
#
# @bug
# @todo
#

# IMPORTS ###########################################################
import os
import plai.workspace.init

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# MAIN ##############################################################
if __name__ == '__main__':

  # Init variables
  ws_root = plai.workspace.init.get_ws_path()
  test_counter = 0
  failed_test_counter = 0

  # Run all unittests in this repo
  for root, dirs, files in os.walk(ws_root):

      # Skip .git directory for search
      if '.git' in dirs:
        dirs.remove('.git')

      # Skip folders that are not "test" or "tests"
      if not root.endswith("test") and not root.endswith("tests"): 
        continue

      # Run all python scripts named "test_*.py|
      for filename in files:
        
        if filename.startswith("test_") and filename.endswith(".py"): 
            print(f"{bcolors.OKBLUE}Running unittest: %s{bcolors.ENDC}" % (filename))
            print(f"{bcolors.OKBLUE}...located: %s{bcolors.ENDC}" % (root))
            test_counter+=1
            
            # Check if unittest successful
            if os.system("python3 " + os.path.join(root, filename)) == 0:
              print(f"{bcolors.OKGREEN}...SUCCESS!{bcolors.ENDC}")
            else:
              print(f"{bcolors.FAIL}...FAILED!{bcolors.ENDC}")
              failed_test_counter+=1
            continue
        else: # not a python unittest
            continue
  
  # Print summary for user
  print("----------------------------------------------------------------------")
  if failed_test_counter != 0:
    print(f"{bcolors.FAIL}%d of %d unittests failed!{bcolors.ENDC}" % (failed_test_counter, test_counter))

  else:
    print(f"{bcolors.OKGREEN}%d unittests successfully terminated!{bcolors.ENDC}" % (test_counter))
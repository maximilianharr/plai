#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color

# Greetings
printf "${NC}--------------------------------------------------${NC}\n"
printf "${RED}Hello $(whoami)! Welcome to $(hostname -s)!${NC}\n"
printf "${NC}--------------------------------------------------${NC}\n"

# Commands
cd /home/kenobi/workspace
source plai/setup.bash
jupyter-notebook --port 8891 --ip 0.0.0.0 --NotebookApp.token='maytheforce'
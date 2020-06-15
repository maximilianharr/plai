#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color

# Greetings
printf "${NC}--------------------------------------------------${NC}\n"
printf "${RED}Hello $(whoami)! Welcome to $(hostname -s)!${NC}\n"
printf "${NC}--------------------------------------------------${NC}\n"

# Commands
cd /home/$(whoami)/workspace
source plai/setup.bash
printf "${RED} Success ${NC}\n"
import os
import sys

while(True):
    # cntrl-c to quit
    command = raw_input('[ep03-so]$ ')
    if command == "exit":
        sys.exit(0)
    command = command.split()

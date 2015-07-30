#!/usr/bin/python3
from notes import Notes, firstrun
import os
import sys

## important stuff
secrets ="""  _________                            __          
 /   _____/ ____   ___________   _____/  |_  ______
 \_____  \_/ __ \_/ ___\_  __ \_/ __ \   __\/  ___/
 /        \  ___/\  \___|  | \/\  ___/|  |  \___ \ 
/_______  /\___  >\___  >__|    \___  >__| /____  >
        \/     \/     \/            \/          \/ 
"""

# intialization control flow
def main():
    if not os.path.isfile(os.environ['HOME'] + "/.secrets/config"):
        if len(sys.argv) > 1:
            if (sys.argv[1] == "init"):
                print("\twelcome to")
                print(secrets)
                firstrun()
        else:
            print(secrets)
            print("\t\tis not initialized. Pass 'init' to set up")
    # the rest of the options
    else:
        notes = Notes()

        if len(sys.argv) > 1:
            if (sys.argv[1] == "init"):
                print(secrets)
                print("\t\tis already set up!")
            elif (sys.argv[1] == "list"):
                print("\tyour")
                print(secrets)
                notes.listnotes()
            elif (sys.argv[1] == "new"):
                if len(sys.argv) > 2:
                    if sys.argv[2] in notes.notes:
                        notes.editnote(sys.argv[2])
                    else:
                        notes.newnote(sys.argv[2])
                else:
                    print("Error: give it a title!")
            elif (sys.argv[1] == "echo"):
                if len(sys.argv) > 2:
                    notes.echonote(sys.argv[2])
            elif (sys.argv[1] == "delete"):
                if len(sys.argv) > 2:
                    notes.deletenote(sys.argv[2])
            else:
                if (sys.argv[1] in notes.notes.keys()):
                    notes.editnote(sys.argv[1])
                else:
                    notes.newnote(sys.argv[1])
        else:
            print(secrets)
            print("\ttry secrets list")
            print("\tor secrets foo")
        notes.close()

if __name__ == '__main__':
    main()

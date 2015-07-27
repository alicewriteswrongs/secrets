from notes import Notes, firstrun
import notes
import os
import sys

# intialization control flow
if not os.path.isfile(os.environ['HOME'] + "/.secrets/config"):
    if len(sys.argv) > 1:
        if (sys.argv[1] == "init"):
            firstrun()
    else:
        print("Secrets is not initialized. Pass 'init' to set up")
# the rest of the options
else:
    notes = Notes()

    if len(sys.argv) > 1:
        if (sys.argv[1] == "init"):
            print("Error: already set up")
        elif (sys.argv[1] == "list"):
            notes.listnotes()
        elif (sys.argv[1] == "new"):
            if len(sys.argv) > 2:
                notes.newnote(sys.argv[2])
            else:
                print("Error: give it a title!")



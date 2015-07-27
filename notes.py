from gnupg import GPG
import sys
import json
import os
import subprocess
import tempfile

def firstrun():
    print("Ok we need to set up some things real quick\n")
    gnupgdir = input("Where's your gnupg config directory?: ")
    identity = input("What's your private key fingerprint?: ")
    if not os.path.isdir(os.environ['HOME'] + "/.secrets"):
        os.mkdir(os.environ['HOME'] + "/.secrets")
    with open(os.environ['HOME'] + "/.secrets/config", "w") as myfile:
        json.dump({'gpghome': gnupgdir, 'identity': identity}, myfile)
    print("Should be all set up! Config in ~/.secrets/config")
    print("Try 'secrets' or 'secrets help' for more!")

class Notes(object):
    def __init__(self):
        self.filepath = os.environ['HOME'] + "/.secrets"
        with open(self.filepath + "/config") as myfile:
            self.config = json.load(myfile)
        self.gpg = GPG(homedir = self.config['gpghome'])
        if (os.path.isfile(self.filepath + "/notes")):
            with open(self.filepath + "/notes") as myfile:
                self.notes = json.load(myfile)
        else:
            self.notes = {}

    def listnotes(self):
        for key in self.notes.keys():
            print(key)

    def newnote(self, note):
        self.notes[note] = ''
        self.editnote(note)

    def editnote(self, note):
        temp = tempfile.mkstemp()
        with open(temp[1], "w") as myfile:
            myfile.write(self.notes[note])
        p = subprocess.Popen((os.environ['EDITOR'], temp[1]))
        p.wait()
        with open(temp[1]) as myfile:
            self.notes[note] = myfile.read()
        os.remove(temp[1])

    def close(self):
        with open(self.filepath + "/notes", "w") as myfile:
            json.dump(self.notes, myfile)


#     def listen(self):

#     def firstrun(self):

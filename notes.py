import gnupg
import json
import os
import subprocess
import tempfile

def firstrun():
    print("Ok we need to set up some things real quick\n")
    gnupgdir = input("Where's your gnupg config directory?: ")
    identity = input("What's your GPG identity?: ")
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
        self.gpg = gnupg.GPG(gnupghome = self.config['gpghome'])
        if (os.path.isfile(self.filepath + "/notes")):
            with open(self.filepath + "/notes") as myfile:
                rawnotes = myfile.read()
            self.notes = json.loads(str(self.gpg.decrypt(rawnotes)))
        else:
            self.notes = {}

    def listnotes(self):
        for key in self.notes.keys():
            print('\t' + key)

    def deletenote(self, note):
        if note in self.notes:
            del self.notes[note]
            print("removed " + note)
        else:
            print("didn't find that one!")

    def newnote(self, note):
        self.notes[note] = ''
        self.editnote(note)

    def editnote(self, note):
        if note in self.notes:
            temp = tempfile.mkstemp()
            with open(temp[1], "w") as myfile:
                myfile.write(self.notes[note])
            p = subprocess.Popen((os.environ['EDITOR'], temp[1]))
            p.wait()
            with open(temp[1]) as myfile:
                self.notes[note] = myfile.read()
            os.remove(temp[1])
        else:
            self.newnote(note)

    def close(self):
        jsonnotes = json.dumps(self.notes)
        encrypted = self.gpg.encrypt(jsonnotes, self.config['identity'])
        with open(self.filepath + "/notes", "w") as myfile:
            myfile.write(str(encrypted))

    def echonote(self, note):
        print(self.notes[note])

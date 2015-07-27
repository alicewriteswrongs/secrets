#Secrets

Secrets is a little Python wrapper around gpg to automate encrypted
notekeeping. You need to already have a gpg key (I wrote a [guide to
gpg](https://github.com/aliceriot/gpg_workshop/blob/master/gpg.markdown)
if you haven't got one) and you need to have your gpg configured to use
gpg-agent (allows the key to be unlocked and stay open for a bit).

##Installing

Cool! There's only one dependency right now, so just do

```
pip install -r requirements.txt
```

Everything else is from the Python 3 standard library. If you want to make
secrets a  little bit easier to use I'd recommend doing something to
add the script to your `$PATH`.

##Keeping super secret notes!

To start off you should do 

```
secrets init
```

to configure the program. Then to list your notes:

```
secrets list
```

to see your secrets (titles only).

```
secrets new foo
```

Secrets will open the notes in your `$EDITOR`. If you haven't set that
before it's probably Vim or nano?

To add a new secret (foo)

```
secrets delete foo
```

to get rid of useless secrets (like foo)

```
secrets echo foo
```

to put the contents of foo on `stdout`, and finally

```
secrets foo
```

to edit foo. Nice!

##Warnings and disclaimers and blah

I'm not a cryptographer or security expert. This program certainly has
some security flaws. Don't use it if you adversary is more technically
sophisticated than 'your roommate snooping through your recent documents'.

In particular I made several decisions which are not secure - the contents
of the notes live in files in `/tmp` in plaintext while you're editing
them. The whole notes database is also in memory when the program is
running. Oops!

Happy secreting!

#Secrets

Secrets is a little Python wrapper around gpg to automate encrypted
notekeeping. You need to already have a gpg key (I wrote a [guide to
gpg](https://github.com/aliceriot/gpg_workshop/blob/master/gpg.markdown)
if you haven't got one) and you need to have your gpg configured to use
gpg-agent (allows the key to be unlocked and stay open for a bit).

Cool!

To use it do:

```
secrets --list
```

to see your secrets (titles only).

```
secrets --new foo
```

to add a new secret (foo)

```
secrets --delete foo
```

to get rid of useless secrets (like foo)

```
secrets --echo foo
```

to put the contents of foo on `stdout`, and finally

```
secrets foo
```

to edit foo. Nice!

##Warnings and disclaimers and blah

I'm not a cryptographer or security expert. This program certainly has
some security flaws. Don't use it if you adversary is more technically
sophisticated than 'your roommate looking at recent documents'.

Happy secreting!

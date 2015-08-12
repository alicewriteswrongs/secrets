##### Signed by https://keybase.io/aliceriot
```
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v2

iQIcBAABCAAGBQJVy66aAAoJEBSAwz4pIHpRisMP/jdkMb6xv5NhBXz8tZ5ir7Ct
SJTWxmfSy3PMfmAGAzDZmJ3VQsWQDQ7yfqsXf/qfN/H09TDl2ahgSKx5krp3YNO9
/A0NnVOpzia+Z5uk4QuLO4aXEv7r4PezNUdCZrHzAwHYM1BpM2bACufBS0hN9Ly6
KR1by0l2E2E5GVtCEiRvfd0h6Y5roh98I1YLw+jCit5U//sWPS4b7RI2JYMViYxk
gM57nbV0Wa1hiy6WTW1sdUxc5++vAoqZxlWPhSNsDBNC/x44lzAciYrhvWxlXt6A
xbxkt6o3mUsJD0Zz2m+PiZWhfDQQkZJAPtX9bCz82c4FSjz1iqVOFZ2ylvfW2USu
R9nfsu+/FleVb28tbkdlU5aqDqVqI7+VEXBr+vrxWIYykN51cpuge0ABB12ISpgB
9QWwr+qHSKqvVdTv9JiaKRyswtq1rblcwIxuT+UoBREWcQrxmTk7g/nXCcoS3URI
CJn6wce3lztknF2VTmPpz8PAAQBhegIagUK3nBFjw8Icum8kAzHi080nuRDTf1ud
SwkPM8GtAf78VzIeNo3P3JOJ97TtVCMkrfNEMnORALK6tSdfbTQaCjDWNVaqhwDR
7APgJ+S+Nm6VZ/cbImEsh9rYQSc4fRZ4lIR3yiPIIYkS1TsPQgHdhlng4k6C/ABF
tezDouXBx5Li9HcyHcrG
=Xzbi
-----END PGP SIGNATURE-----

```

<!-- END SIGNATURES -->

### Begin signed statement 

#### Expect

```
size  exec  file                  contents                                                        
            ./                                                                                    
145           .gitignore          38ef9cba17bb6515d0cc1873d00c3c16416005384cfa8694a77038790603262b
102           .pypirc             0fd801bd08282dc58cb1b94e26399257350dbe762df5a93f2a5db5e8a1beb37f
52            MANIFEST            67b5fe3ff00f64899ee5f9ac54cbf160bb29adb1f0e3a161cb282d65db36e988
2276          README.md           c98423f0f41026688ca66c333a880c9f15e686bb020e53f32f9d7b6c0ce2f352
              __pycache__/                                                                        
              debian/                                                                             
144             changelog         e21f2e4258dd9892aebf4c628c08da24272aae34a9dc77c67d94225c2d100999
1               compat            19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7
435             control           08befa5da37ba03298a243e8a480883650dea4b22c701dd44f9192821cfdfe4e
48              links             8fe786e0bbf6192c697a5bf7e130114e4d49dc332d683f85bacc5e7672bf2295
291   x         rules             300dbfaf20b7d58f2bff74f4a9bb7a5b78c9402391edde7d6969531a4fc6de72
345             secrets.triggers  53fb4129e1b4c0b744acff742b0ea52a5a0a1a38d381fc6605b5475060938b86
2288          notes.py            b0501b5667d90afdb6b704113b31bde5f924fd2fba36341206f32867246c771e
20            requirements.txt    026db7d1dbfc3df78bff6e932836f30350e15bc52732a222a8d0da6f6e41b0a3
              secrets/                                                                            
2124  x       secrets.py          af026ac150fc901bfc6af98190d60d5f57b080429d7589e359eff1441f8dbb0c
593           setup.py            7acbb5fa9d6d6ede22f3b295fa1eba7214b8a24a09d75e42a0a3aa1eac709309
              tests/                                                                              
0               __init__.py       e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
38              test_module.py    aaa54f5935c390f620263162e4dfe8817fd661e86109e8fd9964714145404f36
```

#### Ignore

```
/SIGNED.md
```

#### Presets

```
git      # ignore .git and anything as described by .gitignore files
dropbox  # ignore .dropbox-cache and other Dropbox-related files    
kb       # ignore anything as described by .kbignore files          
```

<!-- summarize version = 0.0.9 -->

### End signed statement

<hr>

#### Notes

With keybase you can sign any directory's contents, whether it's a git repo,
source code distribution, or a personal documents folder. It aims to replace the drudgery of:

  1. comparing a zipped file to a detached statement
  2. downloading a public key
  3. confirming it is in fact the author's by reviewing public statements they've made, using it

All in one simple command:

```bash
keybase dir verify
```

There are lots of options, including assertions for automating your checks.

For more info, check out https://keybase.io/docs/command_line/code_signing
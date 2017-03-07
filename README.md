# FreeMobileSms

Sends SMS using a Free Mobile feature. The SMS can only be send to a phone from the same phone.

It uses URL like this one: https://smsapi.free-mobile.fr/sendmsg?user=USER&pass=PASS&msg=ping

## Usage
You can either launch it and provide what is needed. Or you can build a configuration file _freesms.cfg_, like this one:

```
[FreeSms]
user: ***********
pass: ***********
```

## Python class
```Python
#!/usr/bin/python3

import FreeMobileSms

sms = freeMobileSms.FreeSms(input('user: '), input('pass: '))
sms(input('message: '))
```

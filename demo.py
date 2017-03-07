#!/usr/bin/python3

import FreeMobileSms

sms = FreeMobileSms.FreeSms(input('user: '), input('pass: '))
sms(input('message: '))


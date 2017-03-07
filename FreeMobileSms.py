#! /usr/bin/python3

#  DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004
#
#  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.
#
#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#   0. You just DO WHAT THE FUCK YOU WANT TO.
#
# © Christophe HENRY -- http://sbgodin.fr/

from urllib.request import urlopen
from urllib.parse import urlencode
import time
import os
from configparser import ConfigParser

class FreeSms:

    FREE_URL = 'https://smsapi.free-mobile.fr/sendmsg?'

    def __init__(self, user:str, passw:str, exception = False):
        self.user = user
        self.passw = passw
        self.exception = exception

    def send(self, message:str):
        parameters = {'user': self.user, 'pass': self.passw, 'msg': message}
        url = self.FREE_URL + urlencode(parameters)
        try:
            urlopen(url)
        except Exception as e:
            if self.exception:
                raise e
            else:
                return False
        return True


    def __call__(self, message:str):
        return self.send(message)

    @classmethod
    def load(cls, fileName:str, exception = False):
        """ Sample file:
                [FreeSms]
                user = 99999999
                pass = password
        """

        try:
            config = ConfigParser()
            config.read(fileName)
            user = config.get('FreeSms', 'user')
            passw = config.get('FreeSms', 'pass')
            return cls(user, passw, exception)
        except:
            return False

if __name__ == '__main__':
    user = input('user or config file: [freesms.cfg]: ')
    if not user: user = os.path.dirname(os.path.abspath(__file__))+'/freesms.cfg'
    sms = FreeSms.load(user) # Try to load the config file
    if not sms: # Then it was not a file, treat as a username then ask for a password
        passw = input('pass: ')
        sms = FreeSms(user, passw)

    message = input('message: ')
    if message:
        print('The following message is going to be sent:')
        print("====\n"+message+"\n====")
        if input('Sure (Y/N)? ')=='Y':
            if sms(message):
                print('Message sent!')
            else:
                print('Message not sent, problem occured.')
        else:
            print('Nothing\'s done!')


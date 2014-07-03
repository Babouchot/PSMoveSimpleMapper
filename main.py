#! /usr/bin/python

# System imports
from os import sys
sys.path.append('./PyUserInput/')


# PyUserInput imports
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

# x_dim, y_dim = m.screen_size()
# m.click(x_dim/2, y_dim/2, 1)
# m.click(1200, 565, 1)
# k.type_string('Hello, World!')


# pressing a key
# k.press_key('H')
# which you then follow with a release of the key
# k.release_key('H')
# or you can 'tap' a key which does both
# k.tap_key('e')
# note that that tap_key does support a way of repeating keystrokes with a interval time between each
# k.tap_key('l',n=2,interval=5)
# and you can send a string if needed too
# k.type_string('o World!')
# k.tap_key('1')
# k.tap_key('a')

# k.tap_key(k.windows_l_key)
x, y = m.position()
m.move(x+300, y)

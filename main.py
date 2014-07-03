#! /usr/bin/python


########################## Imports #################################

# System imports
from os import sys
import time

sys.path.append('./PyUserInput/')

sys.path.append('/home/babouchot/workspace/psmoveapi/build')


# PyUserInput imports
from pymouse import PyMouse
from pykeyboard import PyKeyboard

# PSMoveAPI
import psmove

#Qt
from PyQt4 import QtCore, QtGui
from mainWindow import Ui_MainWindow



################################# Class ################################


class MainWindow (QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


# if __name__ == "__main__":
#     app = QtGui.QApplication(sys.argv)
#     myapp = MainWindow()
#     myapp.show()
#     sys.exit(app.exec_())






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
# x, y = m.position()
# m.move(x+300, y)


nb = psmove.psmove_count_connected()
print("Nb moves connected : " + str(nb))

move = psmove.PSMove()
tracker = psmove.PSMoveTracker()

tracker.set_mirror(True)

# Calibrate the controller with the tracker
result = -1
while result != psmove.Tracker_CALIBRATED:
    print 'Trying to calibrate...'
    result = tracker.enable(move)

auto_update_leds = tracker.get_auto_update_leds(move)
print 'Auto-update LEDs is', ('enabled' if auto_update_leds else 'disabled')



while True:

    while move.poll() : pass

    tracker.update_image()
    tracker.update()

    # Check the tracking status
    status = tracker.get_status(move)
    if status == psmove.Tracker_TRACKING:
        x, y, radius = tracker.get_position(move)
        # print 'Position: (%5.2f, %5.2f), Radius: %3.2f, Trigger: %3d' % (
                # x, y, radius, move.get_trigger())
        m.move(x*3,y*3)
        pressed, released = move.get_button_events()
        buttons = move.get_buttons()


        scrollDirection = 1 if buttons & psmove.Btn_TRIANGLE else -1
        m.scroll(scrollDirection * move.get_trigger() / 20)

        if pressed & psmove.Btn_MOVE:
            m.click(x*3,y*3)
        # elif buttons & psmove.Btn_MOVE:
        #     m.drag(x*3,y*3)

        if pressed & psmove.Btn_SELECT:
            k.tap_key(k.windows_l_key)

        if pressed & psmove.Btn_CIRCLE:
            m.click(x*3,y*3, 2)

        if pressed & psmove.Btn_CROSS:
            k.tap_key(k.enter_key)

        if pressed & psmove.Btn_SQUARE:
            k.tap_key(k.tab_key)


    elif status == psmove.Tracker_CALIBRATED:
        print 'Not currently tracking.'
    elif status == psmove.Tracker_CALIBRATION_ERROR:
        print 'Calibration error.'
    elif status == psmove.Tracker_NOT_CALIBRATED:
        print 'Controller not calibrated.'



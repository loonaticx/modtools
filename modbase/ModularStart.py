# This is the file that gets imported by the Launcher as soon as phase 3 is
# complete. This will happen once during the install/download process as soon
# as phase 3 is finished downloading. When the Launcher is run after the
# download/install is complete, it will import this file after realizing
# phase 3 is already complete.
#
#
# Note: you can run this standalone by letting the launcher default to None
#   from toontown.toonbase.ToontownStart import *
#


# This module redefines the builtin import function with one
# that prints out every import it does in a hierarchical form
# Annoying and very noisy, but sometimes useful
# import VerboseImport

# Need to import builtins and use the builtins.foo = x
# technique here in case you start toontown from the command line
import builtins

class game:
    name = "toontown"
    process = "client"
builtins.game = game()

import time
import os
import sys
import random
from panda3d.core import *

"""
You may need to edit this file depending on where your prc file is located.
"""
loadPrcFile('etc/Configrc.prc')
loadPrcFileData("", "model-path resources")
loadPrcFileData("", "default-model-extension .bam")


# See if we have a launcher, if we do not, make an empty one
try:
    launcher
except:
    from toontown.launcher.ToontownDummyLauncher import ToontownDummyLauncher
    launcher = ToontownDummyLauncher()
    builtins.launcher = launcher


# Default to "normal" web exit page.  This should be set early
# so that the right thing will get done on a crash.  "normal"
# may be marketting info, thanks for playing, or the report
# bug page.  The installer.php file will use this setting.
launcher.setRegistry("EXIT_PAGE", "normal")

# The first thing we need to do is make sure the Flash intro is not playing
# If it is, we need to wait here until it is done. We check to see if it is
# done by asking the Launcher.

pollingDelay = 0.5

print('ToontownStart: Polling for game2 to finish...')
while (not launcher.getGame2Done()):
    time.sleep(pollingDelay)
print('ToontownStart: Game2 is finished.')

# Ok, now we know we are clear from the flash into, fire it up
print('ToontownStart: Starting the game.')

# depending on what your build is, we may or may need these guys:
try:
    from otp.otpbase.OTPModules import *
    # Toontown specific modules
    from panda3d.toontown import *
except:
    pass

from panda3d.core import Loader as PandaLoader

if launcher.isDummy():
    # Create a dummy HTTPClient so we can get that stupid openSSL
    # random seed computed before we attempt to open the window.  (We
    # only need do this if we don't have a launcher.  If we do have a
    # launcher, it's already been created.)
    http = HTTPClient()
else:
    http = launcher.http

from direct.gui import DirectGuiGlobals
print('ToontownStart: setting default font')
from toontown.toonbase import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)

# Set the error code indicating failure opening a window in case we
# crash while opening it (the GSG code will just exit if it fails to
# get the window open).
launcher.setPandaErrorCode(7)

# Ok, we got the window open.
launcher.setPandaErrorCode(0)
# Tell the launcher that our panda window is open now so
# it can tell the browser and flash to shutdown
launcher.setPandaWindowOpen()

# Open our debug tools if we have them.
if __debug__ and ConfigVariableBool('want-debug-tools', False).getValue():
    from toontown.toonbase import ToontownDebugTools
    debugTools = ToontownDebugTools.ToontownDebugTools()
    debugTools.start()

# Also, once we open the window, dramatically drop the timeslice
# for decompressing and extracting files, so we don't interfere
# too much with rendering.
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)

# todo: move these to ModularBase
# DirectGuiGlobals.setDefaultRolloverSound(base.loader.loadSfx("phase_3/audio/sfx/GUI_rollover.mp3"))
# DirectGuiGlobals.setDefaultClickSound(base.loader.loadSfx("phase_3/audio/sfx/GUI_create_toon_fwd.mp3"))
# DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))

"""
Example Usage + Notes
"""

# You'd put this chunk on the top of the file, preferably before all the other imports.
if __name__ == "__main__":
    # VVVV Uncomment me VVVV
    # from modtools.toontown.toonbase import ModularStart

    # You can either run ModularBase or ToonBase. Either one will work! (Preferably ModularBase, though.)
    from modtools.toontown.toonbase.ModularBase import ModularBase

    # Very important that you set base to this within the module.
    base = ModularBase()

    # We can call some extra methods if we need them for our instance:
    base.initCR()  # Initialize Client Repository (defines base.cr)
    base.startConnection()  # Loads in our client into the PAT screen, as it does usually.

###

# You'd put this chunk on the bottom of the file, outside any class/function scope.
if __name__ == "__main__":
    # Put whatever you wanna call here (preferably related to the module you're putting this into)
    # Ex: toontown/suit/Suit.py

    # from toontown.suit import Suit
    # s = Suit.Suit()
    # from toontown.suit import SuitDNA
    # d = SuitDNA.SuitDNA()
    # d.newSuit('tbc')
    # s.setDNA(d)
    # s.loop('neutral')
    # s.reparentTo(render)
    # s.setPos(0, 0, 0)
    # base.oobe()

    # Lastly, we need to call this for anything to pop up.
    base.run()


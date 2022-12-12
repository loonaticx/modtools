from modtools.toontown.toonbase import ModularStart
from modtools.toontown.toonbase.ModularBase import ModularBase

base = ModularBase()
base.initCR()

base.generateLocalAvatar()
base.localAvatar.reparentTo(render)
base.localAvatar.hp = 15  # hack
testModel = loader.loadModel("phase_4/models/neighborhoods/toontown_central")
testModel.reparentTo(render)

# base.modular = False
# base.startConnection()

base.oobe()
base.run()

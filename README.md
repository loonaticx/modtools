# Toontown Modtools
**modtools** is a special template repository module that allows you to write and execute programs outside of the normal Toontown interface. By default, it still launches Toontown, but you're met with an empty void rather than seeing the connection screen.

You can think of this as a dummy Toontown client. It loads in all the barebones required to launch the game, and that's it. Using this system, you can make calls to certain Toontown modules to "emulate" certain features of the game, such as instantiating GUI classes and most DistributedObjects.

## Features
- Rapid prototyping support! You can easily generate core features at will, such as the ClientRepository and a controllable localAvatar.
- Feasible client-sided testing on graphical components, such as GUI, models, animations, etc.
- Easy client-sided debugging. You can theoretically create and load Hoods, Loaders, DistributedObject instances, etc.

## Limitations
- Some assembly required: Since not all Toontown projects run the same, you may still need to adjust your codebase to support certain features. You can check out more information on the Wiki.
- *Very* limited AI support. In order to simulate AI, you must merge all of the AI code into the client-sided code-- preferably doing this in a new file. There's a lot of hacks that you may need to apply in this regard.
	- No support for dealing with DelayDelete calls; you must temporarily comment them out in your codebase as a workaround.


# Installation

- ``git clone`` this in your root Toontown directory.
- If applicable, copy the ``modtools.vspec`` file into the ``vspec`` directory if you have one. If you don't, ignore this step.
- If you already have a modtools extension (such as ``toon_snapshot``), ``git clone`` that repository within the modtools folder.


## Usage
For creating custom modules with modtools, check the wiki.

Note: It's recommended you document your modules to avoid abstraction.


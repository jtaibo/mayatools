# Maya Tools

## Installation

1. Clone or unzip the mayatools repository in a "scripts" directory in Maya search path (e.g. ~Documents/maya/2019/scripts)
2. Copy shelf/ directory contents in ~Documents/maya/2019/prefs/shelves/
    or execute install.bat script
3. Start Maya. A new MTools shelf should appear

## Tools

All the tools below are accessible as buttons in the MTools shelf

### Replicator

Pressing the shelf button will open the Replicator dialog pictured below

![Replic8r UI](/images/replic8r_ui.jpg)

Select the element to replicate, select the curve path, adjust increment and node name, and press replicate button.
The increment is the separation between repetitions, in percentage of the total length of the curve.

### UV transferator

Transfer UV sets and color sets (if any) from first selected element to all other elements in selection.

First select the original element (with the right UVs), then add to the selection all other elements. Finally press the "UVxfr8r" button in the shelf

### Texture renombrator

Remove file textures path until "sourceimages/" (inclusive) to convert absolute to relative paths

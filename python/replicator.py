import maya.cmds as cmd


################################################################################
# Replicate selected element along the last-selected curve
################################################################################
def doReplicate():

    the_name = cmd.textFieldGrp("name", query=True, text=True)
    the_incr = cmd.floatSliderGrp("incr", query=True, value=True)

    selection = cmd.ls(selection=True, long=True)
    
    element = selection[0]
    curve = selection[1]
    
    # Build motion path
    the_motion_path = cmd.pathAnimation( element, curve=curve, fractionMode=True, follow=True, followAxis="z", upAxis="y", startTimeU=1, endTimeU=100 )
    
    # Flat animation curves
    cmd.keyTangent(the_motion_path, inTangentType="linear", outTangentType="linear")
    
    # Create animation snapshot
    the_snapshot = cmd.snapshot(element, name=the_name, endTime=100, increment=the_incr)


################################################################################
# Build the user interface
################################################################################
def buildUI():

    window = cmd.window( title="Replicator", iconName='replic8r', widthHeight=(400, 210) )
    column = cmd.columnLayout( columnAttach=("both",10), columnAlign="center", adjustableColumn=True)

    cmd.separator(height=10)  
    cmd.text(label="REPLICATOR")
    cmd.separator(height=10)  
    cmd.text(label="Select the element to replicate,\nselect the curve to replicate it along,\nset the separation between elements (increment),\nand press Replicate button")
    cmd.separator(height=10)
    
    cmd.textFieldGrp("name", label="Name", text="chain", editable=True)
    cmd.floatSliderGrp("incr", label="Increment", min=0, max=10, fieldMaxValue=100, field=True, value=1.0)

    cmd.separator(height=10)
    
    cmd.button( label='Replicate', command=("mayatools.python.replicator.doReplicate()") )
    cmd.button( label='Close', command=('maya.cmds.deleteUI(\"' + window + '\", window=True)') )

    # Set its parent to the Maya window (denoted by '..')
    cmd.setParent( '..' )
    # Show the window that we created (window)
    cmd.showWindow( window )


################################################################################
# Entry point - replicator.replicate()
################################################################################

def replicate():
	buildUI()

print("Replicator imported")

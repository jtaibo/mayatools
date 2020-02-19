import maya.cmds as cmd

def uvtransfer():
    # Store original selection
    selected = cmd.ls(sl=True)

    # Separate first selected element (source) from others (targets)
    targets = cmd.ls(sl=True)
    source = targets.pop(0)

    for object in targets:
        cmd.select([source, object])
        # sampleSpace = 4 (0 is world space, 1 is model space, 4 is component-based, 5 is topology-based)
        # transferUVs = 2 (all UV sets are transferred)
        # transferColors = 2 (all color sets are transferred)
        cmd.transferAttributes(sampleSpace=4, transferUVs=2, transferColors=2)

    # Restore original selection
    cmd.select(selected)

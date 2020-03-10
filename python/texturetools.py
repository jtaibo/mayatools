import maya.cmds as cmd

###############################################################################
#    Remove path prefix from texture files
###############################################################################
def removePrefixFromTexturePath(prefix):

    #textures = cmd.ls(textures=True)
    textures = cmd.ls(type="file")
    
    for tex in textures:
        path = cmd.getAttr(tex + ".fileTextureName")
        if path.startswith(prefix):
            trimmed_path = path[len(prefix):]
            print("PREFIX FOUND - converting ", path, " to ", trimmed_path)
            cmd.setAttr(tex + ".fileTextureName", trimmed_path, type="string")


###############################################################################
#    Remove path till "sourceimages" folder (inclusive)
###############################################################################
def clipTexturePathToSourceImages():

    keyword = "sourceimages/"

    textures = cmd.ls(type="file")

    for tex in textures:
        path = cmd.getAttr(tex + ".fileTextureName")
        idx = path.find(keyword)
        if idx != -1:
            trimmed_path = path[idx+len(keyword):]
            print("Correcting ", path, " to ", trimmed_path)
            cmd.setAttr(tex + ".fileTextureName", trimmed_path, type="string")

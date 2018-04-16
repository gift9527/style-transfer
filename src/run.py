import sys
import os

filePath = os.getcwd()
# os.system("cd " + filePath)
pythonfile = "evaluate.py"
originImgPath = "/Users/taoming/Downloads/WX20180414.jpg"
styledImgPath = originImgPath[:-4] + "Styled" + ".jpg"
ModelsDirPath = filePath[:-3] + "Models"

ModelsListName = os.listdir(ModelsDirPath)

# models option
# 'scream.ckpt', 'wave.ckpt', 'rain_princess.ckpt', 'la_muse.ckpt', 'wreck.ckpt', 'udnie.ckpt'

def StyleImg(modelStyle, originImgPath, styledImgPath):
    print "Now Support:"
    print ModelsListName
    print "U chose " + modelStyle
    os.system(
        "python " + filePath + "/" + pythonfile + " --checkpoint " + ModelsDirPath + "/" + modelStyle + " --in-path " + originImgPath + " --out-path " + styledImgPath)
    print "Mission Completed"

# example
#StyleImg('rain_princess.ckpt', originImgPath, styledImgPath)

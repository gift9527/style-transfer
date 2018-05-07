import sys
import os
import scipy.misc

filePath = os.getcwd()
# os.system("cd " + filePath)
pythonfile = "evaluate.py"
originImgPathTest = "/Users/taoming/Downloads/WX20180414.jpg"
outImgPathTest = originImgPathTest[:-4] + "Fited" + ".jpg"
styledImgPathTest = originImgPathTest[:-4] + "Styled" + ".jpg"
ModelsDirPath = filePath[:-3] + "Models"

ModelsListName = os.listdir(ModelsDirPath)


# models option
# 'scream.ckpt', 'wave.ckpt', 'rain_princess.ckpt', 'la_muse.ckpt', 'wreck.ckpt', 'udnie.ckpt'

def fitImageSize(originImagePath, outImagePath):
    img = scipy.misc.imread(originImagePath, mode='RGB')
    print img.shape

    percent = 100
    rawSizeAera = img.shape[0] * img.shape[1]
    fitSizeAera = rawSizeAera
    # 700 * 1000 can pass, bigger than this size may cause error
    while True:
        if fitSizeAera > 700000.0:
            percent = percent - 1
            fitSizeAera = rawSizeAera * pow(percent,2) / 10000.0
        else:
            break
    imgFit = scipy.misc.imresize(img, percent)
    scipy.misc.imsave(outImagePath, imgFit)


def StyleImg(modelStyle, originImgPath, styledImgPath):
    print "Now Resize Image"
    fitImagePath = originImgPath[:-4] + "Fited" + ".jpg"
    fitImageSize(originImgPath, fitImagePath)
    print "Resize Image Completed"
    print "Now Support:"
    print ModelsListName
    print "U chose " + modelStyle
    command = "python " + filePath + "/" + pythonfile + " --checkpoint " + ModelsDirPath + "/" + modelStyle + " --in-path " + fitImagePath + " --out-path " + styledImgPath + " --batch-size 1"
    print command
    os.system(command)
    print "Mission Completed"


# example
StyleImg('wave.ckpt', originImgPathTest, styledImgPathTest)
# fitImageSize(originImgPath, outImgPath)


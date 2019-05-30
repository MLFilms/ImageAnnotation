import glob
import os
from fileConvert import fileConvert


imgDims = [100,100]
targetDir = "E:/Projects/fake/simulations/fortran\LandauGin/run20190529_144637/data-k-1.00-beta-10.000-mu-0.000"
outDir = "C:\\Users\\Eric Minor\\TrackingML\\defectTracker\\labels\\out"

if not os.path.exists(outDir):
    os.makedirs(outDir)

filePattern = os.path.join(targetDir, '*.txt')   

for filename in glob.glob(filePattern):
    fileConvert(filename,headerLines=1,imgSize=imgDims)


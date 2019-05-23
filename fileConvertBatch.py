import glob
import os
from fileConvertF import fileConvert

targetDir = "C:\\Users\\Eric Minor\\TrackingML\\defectTracker\\labels"
outDir = "C:\\Users\\Eric Minor\\TrackingML\\defectTracker\\labels\\out"

if not os.path.exists(outDir):
    os.makedirs(outDir)

filePattern = 	targetDir+"\\*.txt"   

for filename in glob.glob(filePattern):
    fileConvert(filename,outDir)


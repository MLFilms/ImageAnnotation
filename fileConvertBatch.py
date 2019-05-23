import glob
import os
from fileConvert import fileConvert

targetDir = "C:\\Users\\Eric Minor\\TrackingML\\defectTracker\\labels"
outDir = "C:\\Users\\Eric Minor\\TrackingML\\defectTracker\\labels\\out"

if not os.path.exists(outDir):
    os.makedirs(outDir)

filePattern = os.path.join(targetDir, '*.txt')   

for filename in glob.glob(filePattern):
    fileConvert(filename,headerLines=1)


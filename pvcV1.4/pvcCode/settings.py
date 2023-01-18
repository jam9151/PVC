#reqired libraries  
#pip install openpyxl, pandas, python-barcode, pillow, numpy, datetime, sys
#written by Jesse McNary
import os, sys
from datetime import datetime

#ext
jpg = '.jpg'
png = '.png'
txt = '.txt'
html = '.html'

#suf
frontOfBox = '_front'
backOfBox = '_back'
sideOfBox = '_side'
angleOfBox = '_angle'
barcodePhotoSuf = '_barcode'
adSuf = '_ad'
pageSuf = '_page'

#date
today = datetime.now()
today = today.strftime("%d-%m-%Y(%HH %MM %SS)")

#paths

#mainWorkingDirs
cwd = os.getcwd()
pops = os.path.dirname(cwd)
grandPops = os.path.dirname(pops)
greatGrandPops = os.path.dirname(grandPops) 

#pathToLogsFiles
pathToLogs = os.path.join(pops, "logs")
pathToSystemLogs = os.path.join(pathToLogs,"systemLogs")
pathToSystemLogsTextFile = os.path.join(pathToSystemLogs, today+txt)

#print(pathToSystemLogsTextFile)
pathToShutilLogs = os.path.join(pathToLogs, "shutilLogs")
pathToShutilLogsTextFile = os.path.join(pathToShutilLogs, today+txt)
#print(pathToShutilLogsTextFile)

#path
pathToUpcImagesDir = os.path.join(pops, "siteData/images")
pathToProductsDir = os.path.join(pops, "siteData/products") 
pathToHtmlTemp = os.path.join(cwd, "template.html") 



pathToBarcodeSheet = os.path.join(pops, "siteData/barcodeSheet/barcodeSheet.html")
pathToCssData = os.path.join("barcodeSheetData", "cssData.txt")
pathToJsForBcSheet = os.path.join("barcodeSheetData", "jsForBcSheet.txt")
pathToJsForSearchBar = os.path.join("barcodeSheetData", "jsForSearchBar.txt")

pathToNas = os.path.join(grandPops ,"product_photo_inbox")


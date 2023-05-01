#written by Jesse McNary
import checkTool
import barcodes
import settings
import pageCreator
import sortFiles

import time

startTime = time.time()

def main():
	ctdata = checkTool.checkToolData()

	dfDict = ctdata[0]

	priceDict = ctdata[1]

	valueDict = ctdata[2]

	qtyDict = ctdata[3]
	
	upcList = list(dfDict.keys())
		
	checkForPhotosResult = checkTool.checkForPhotos(upcList)
		
	listForUpcPhotos = checkForPhotosResult[0]
	
	checkTool.checkForDirAndMake(upcList,dfDict,priceDict,listForUpcPhotos)
	
	barcodes.barcodesHandler(upcList, ctdata, checkForPhotosResult)
 
	pageCreator.htmlPageCreator(settings.pathToProductsDir, dfDict, priceDict, upcList, settings.pageSuf,settings.html)
	
	sortFiles.sortFilesToDir(checkForPhotosResult)
		
	return "System Finished"		

if __name__ == "__main__":
    main()

print(f"Program took {time.time() - startTime} seconds to execute")

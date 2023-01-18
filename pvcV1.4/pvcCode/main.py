#written by Jesse McNary
import sys
import check_toolV1 as ct
import bcCreator as bc
import settings as st
import pageCreator as pc
import sortFiles as sf
import barcodeSheetCreator as bsc
import pandas
import os
def checkForPhotos():

	with open(st.pathToSystemLogsTextFile, "a") as f:
		#dirExists = pc.upcDirCheck(st.pathToUpcImagesDir, ct.upcList)
		
		listForBoxPhotosFront = ct.checkTool(st.pathToUpcImagesDir, ct.upcList, st.frontOfBox, st.jpg)
		numOfBoxPhotosFront = len(listForBoxPhotosFront)
		print("Photos missing for _front:\n",numOfBoxPhotosFront,"\n", listForBoxPhotosFront, "\n", file=f)


		listForBoxPhotosSide = ct.checkTool(st.pathToUpcImagesDir, ct.upcList, st.sideOfBox, st.jpg)
		numOfBoxPhotosSide = len(listForBoxPhotosSide)
		print("Photos missing for _back:\n",numOfBoxPhotosSide,"\n", listForBoxPhotosSide, "\n", file=f)


		listForBoxPhotosBack = ct.checkTool(st.pathToUpcImagesDir, ct.upcList, st.backOfBox, st.jpg)
		numOfBoxPhotosBack = len(listForBoxPhotosBack)
		print("Photos missing for _side:\n",numOfBoxPhotosBack,"\n", listForBoxPhotosBack, "\n", file=f)
	

		listForBoxPhotosBack = ct.checkTool(st.pathToUpcImagesDir, ct.upcList, st.angleOfBox, st.jpg)
		df = pandas.DataFrame(listForBoxPhotosBack)
		pandas.set_option('display.float_format', lambda x:'%f' % x)
		df.to_excel(os.path.join(st.pathToNas,"pvcDataExport", "listOfPhotosNeeded.xlsx"), float_format=str)
		
		numOfBoxPhotosBack = len(listForBoxPhotosBack)
		print("Photos missing for _angle:\n",numOfBoxPhotosBack,"\n", listForBoxPhotosBack, "\n", file=f)
		
		listForUpcPhotos = ct.checkTool(st.pathToUpcImagesDir, ct.upcList, st.barcodePhotoSuf, st.png)
		numOfBarcodes = len(listForUpcPhotos)
		print("Barcodes needed:\n", numOfBarcodes,listForUpcPhotos, file=f)

		listForHtml = ct.checkTool(st.pathToProductsDir, ct.upcList, st.pageSuf, st.html)
		numOfHtml = len(listForHtml)
		print(".html files missing:\n", numOfHtml,"\n", listForHtml, "\n", file=f)

		#for sorting files automation
		mvFront = ct.checkForNas(st.pathToNas, ct.upcList, st.frontOfBox, st.jpg)
		#print(mvFront, "\n")

		mvBack = ct.checkForNas(st.pathToNas, ct.upcList, st.backOfBox, st.jpg)
		#print(mvBack, "\n")

		mvSide = ct.checkForNas(st.pathToNas, ct.upcList, st.sideOfBox, st.jpg)
		#print(mvSide,"\n")

		mvAngle = ct.checkForNas(st.pathToNas, ct.upcList, st.angleOfBox, st.jpg)
		#print(mvAngle,"\n")

	f.close()
	return listForUpcPhotos,listForHtml, mvFront, mvBack, mvSide, mvAngle
	

result = checkForPhotos()

#listForUpcPhotos = checkForPhotos()
def checkForDirAndMake():
	pc.upcDirCheck(st.pathToUpcImagesDir, ct.upcList)
	pc.upcHtmlCreator(st.pathToProductsDir, ct.dfDict, result[1],st.pageSuf, st.html)

def barcodesHandler():
	bc.barcodeCreator(result[0], st.barcodePhotoSuf, st.pathToUpcImagesDir)
	bsc.upcBarcodeCreator(ct.upcList, ct.dfDict, ct.priceDict, ct.valueDict, ct.qtyDict)

def sortFilesToDir():
	with open(st.pathToShutilLogsTextFile, "a") as f:
		frontSent = sf.sortFiles(st.pathToNas, result[2], st.frontOfBox, st.jpg)
		print("_front sent", frontSent, "\n", file=f)
		
		sideSent = sf.sortFiles(st.pathToNas, result[3], st.sideOfBox, st.jpg)
		print("_side sent", sideSent, "\n", file=f)

		backSent = sf.sortFiles(st.pathToNas, result[4], st.backOfBox, st.jpg)
		print("_back sent", backSent, "\n", file=f)

		angleSent = sf.sortFiles(st.pathToNas, result[5], st.angleOfBox, st.jpg)
		print("_angle sent", angleSent, "\n", file=f)
	f.close()
#checkForPhotos()
checkForDirAndMake()
barcodesHandler()
sortFilesToDir()


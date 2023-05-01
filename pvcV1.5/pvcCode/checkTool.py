#written by Jesse McNary
import sys
import os
import pandas
import settings as st 
import pageCreator as pc

#variables from settings module

#checkToolData creates the dataframe of UPCs that are needed to be processed
def checkToolData():  
     #file name declared
	xlsxFile = 'psheet.xlsx'

	xlsxFileDataframe = pandas.read_excel(xlsxFile, sheet_name='Walmart')

	df = pandas.DataFrame(xlsxFileDataframe,index=range(300))
	
	df['Unnamed: 10'] = df['Unnamed: 10'].fillna(0)

	df = (df.loc[(df['Unnamed: 7'] == 'y') & (df['Unnamed: 10'] != 0)])

	filteredDataFrame = pandas.DataFrame(df)


	#dfDict, priceDict, valeuDict, and qtyDict are all dictionaries created for the web pages, the UPCs from filteredDataFrame are they keys and the values are item discriptions.
	dfDict = dict(zip(filteredDataFrame['Unnamed: 10'], filteredDataFrame['Unnamed: 2']))

	#filteredDataFrame = pd.DataFrame(dfFiltered)
	
	priceDict = dict(zip(filteredDataFrame['Unnamed: 10'], filteredDataFrame['Unnamed: 5']))

	valueDict = dict(zip(filteredDataFrame['Unnamed: 10'], filteredDataFrame['Unnamed: 6']))

	qtyDict = dict(zip(filteredDataFrame['Unnamed: 10'], filteredDataFrame['Unnamed: 1']))
    	
    #shortUpcDict = dict(zip(filteredDataFrame['Unnamed: 10'], filteredDataFrame['Unnamed: 11']))

	#the final filtered upclist.
	upcList = filteredDataFrame['Unnamed: 10'].tolist()

	#strips white space on the upc to provent data corruption.
	
	numUPC = len(upcList)
	for item in upcList:
		item.strip()
    #returns 4 dictionaries
	return dfDict, priceDict, valueDict, qtyDict

def checkForPhotos(upcList):

	with open(st.pathToSystemLogsTextFile, "a") as f:
		#dirExists = pc.upcDirCheck(st.pathToUpcImagesDir, checkTool.upcList)
		
		listForBoxPhotosFront = checkTool(st.pathToUpcImagesDir, upcList, st.frontOfBox, st.jpg)
		numOfBoxPhotosFront = len(listForBoxPhotosFront)
		print("Photos missing for _front:\n",numOfBoxPhotosFront,"\n", listForBoxPhotosFront, "\n", file=f)


		listForBoxPhotosSide = checkTool(st.pathToUpcImagesDir, upcList, st.sideOfBox, st.jpg)
		numOfBoxPhotosSide = len(listForBoxPhotosSide)
		print("Photos missing for _back:\n",numOfBoxPhotosSide,"\n", listForBoxPhotosSide, "\n", file=f)


		listForBoxPhotosBack = checkTool(st.pathToUpcImagesDir, upcList, st.backOfBox, st.jpg)
		numOfBoxPhotosBack = len(listForBoxPhotosBack)
		print("Photos missing for _side:\n",numOfBoxPhotosBack,"\n", listForBoxPhotosBack, "\n", file=f)
	

		listForBoxPhotosBack = checkTool(st.pathToUpcImagesDir, upcList, st.angleOfBox, st.jpg)
		df = pandas.DataFrame(listForBoxPhotosBack)
		pandas.set_option('display.float_format', lambda x:'%f' % x)
		df.to_excel(os.path.join(st.pathToNas,"pvcDataExport", "listOfPhotosNeeded.xlsx"), float_format=str)
		
		numOfBoxPhotosBack = len(listForBoxPhotosBack)
		print("Photos missing for _angle:\n",numOfBoxPhotosBack,"\n", listForBoxPhotosBack, "\n", file=f)
		
		listForUpcPhotos = checkTool(st.pathToUpcImagesDir, upcList, st.barcodePhotoSuf, st.png)
		numOfBarcodes = len(listForUpcPhotos)
		print("Barcodes needed:\n", numOfBarcodes,listForUpcPhotos, file=f)

		listForHtml = checkTool(st.pathToProductsDir, upcList, st.pageSuf, st.html)
		numOfHtml = len(listForHtml)
		print(".html files missing:\n", numOfHtml,"\n", listForHtml, "\n", file=f)

		#for sorting files automation
		mvFront = checkForNas(st.pathToNas, upcList, st.frontOfBox, st.jpg)
		#print(mvFront, "\n")

		mvBack = checkForNas(st.pathToNas, upcList, st.backOfBox, st.jpg)
		#print(mvBack, "\n")

		mvSide = checkForNas(st.pathToNas, upcList, st.sideOfBox, st.jpg)
		#print(mvSide,"\n")

		mvAngle = checkForNas(st.pathToNas, upcList, st.angleOfBox, st.jpg)
		#print(mvAngle,"\n")

	f.close()
	return listForUpcPhotos,listForHtml, mvFront, mvBack, mvSide, mvAngle



#The purpose of this function is to check whether or not directories exist.
def checkTool(path, upcList, suf, ext):

	returnList = []

	
	if path != st.pathToProductsDir:
		
		for item in upcList:
		
		
			pathToPhoto = os.path.join(path, item, str(item)+suf+ext)			

			#checks if the photo (upc number).JPG exists, returns TRUE if it exists, FALSE else.
			tfPhoto = os.path.exists(pathToPhoto)
			
			if tfPhoto == False:
				returnList.append(item)
	else:
		for item in upcList:
			
			pathToPhoto = os.path.join(path, str(item)+suf+ext)
			
			tfPhoto = os.path.exists(pathToPhoto)
		
			returnList.append(item)
			if tfPhoto == False:
				returnList.append(item)
	
	return(returnList)
	
def checkForNas(path,upcList,suf,ext):

	listForSorting = []
	
	for item in upcList:
		pathToPhoto = os.path.join(path,str(item)+suf+ext)
				

		#checks if the photo (upc number).JPG exists, returns TRUE if it exists, FALSE else.
		tfPhoto = os.path.exists(pathToPhoto)
	  	
		if tfPhoto == True:
			listForSorting.append(item)
	return(listForSorting)

def checkForDirAndMake(upclist,dfDict, priceDict, listForUpcPhotos):
		upcDirCheck(st.pathToUpcImagesDir, upclist)
		pc.htmlPageCreator(st.pathToProductsDir, dfDict, priceDict,listForUpcPhotos,st.pageSuf, st.html)
  
def upcDirCheck(path, upclist):
	for item in upclist:
		
		pathToDir = os.path.join(path, item)
		
		tfDir = os.path.isdir(pathToDir)

		if tfDir == False:
			os.mkdir(pathToDir)
			
	return tfDir

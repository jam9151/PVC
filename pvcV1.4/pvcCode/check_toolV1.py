#written by Jesse McNary
import sys
import os
import numpy as np
import pandas as pd 
import settings as st 

#variables from settings module

#checkToolData creates the dataframe of UPCs that are needed to be processed
def checkToolData():  
     #file name declared
	xlsxFile = 'psheet.xlsx'

	xlsxFileDataframe = pd.read_excel(xlsxFile, sheet_name='Walmart')

	df = pd.DataFrame(xlsxFileDataframe,index=range(300))
	
	df['Unnamed: 10'] = df['Unnamed: 10'].fillna(0)

	dfFiltered = (df.loc[(df['Unnamed: 7'] == 'y') & (df['Unnamed: 10'] != 0)])

	filteredDataFrame = pd.DataFrame(dfFiltered)


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
    #returns all 4 dictionaries
	return dfDict, priceDict, valueDict, qtyDict

#dataResult is list of the 4 dictionaries from checkToolData()
dataResult = checkToolData()
#dictionary for webpage, creates two dictionaries both with the UPC number as the key, and the item discription for the first value, and the price for the second value.

dfDict = dataResult[0]

priceDict = dataResult[1]

valueDict = dataResult[2]

qtyDict = dataResult[3]


upcList = list(dfDict.keys())


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
	print("\n")	
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

#written by Jesse McNary
import settings as st
import os
import check_toolV1 as ct
#from pathlib import Path
import pandas as pd

def upcDirCheck(path, upclist):
	for item in upclist:
		
		pathToDir = os.path.join(path, item)
		
		tfDir = os.path.isdir(pathToDir)

		if tfDir == False:
			os.mkdir(pathToDir)
			
	return tfDir

def upcHtmlCreator(path, dfDict, upcList, suf, ext):
	
	for item in upcList:

		pathToHtml = os.path.join(path, item+suf+ext)
		
		fin = open(st.pathToHtmlTemp)	
		
		fout = open(pathToHtml, "wt")  
		
		for line in fin:
			fout.write(line.replace('_UPC_', str(item)).replace('_DES_', ct.dfDict.get(str(item))).replace('_PRC_', ct.priceDict.get(str(item))))
			
		fin.close()
		
		fout.close()
		

#written by Jesse McNary
import settings as st
import os
import checkTool as ct



def htmlPageCreator(path, dfDict,priceDict, upcList, suf, ext):
	
	for item in upcList:

		pathToHtml = os.path.join(path, item+suf+ext)
		
		fin = open(st.pathToHtmlTemp)	
		
		fout = open(pathToHtml, "wt")  
		
		for line in fin:
			fout.write(line.replace('_UPC_', str(item)).replace('_DES_', dfDict.get(str(item))).replace('_PRC_', priceDict.get(str(item))))
			
		fin.close()
		
		fout.close()
		

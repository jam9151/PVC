#written by Jesse McNary
import settings as st
import checkTool as ct
from datetime import datetime

import sys
import os
from barcode import EAN13
from barcode.writer import ImageWriter
import barcode

#barcodeFormat = barcode.get_barcode_class('ean')

def barcodeCreator(upcList, suf, path):
	for item in upcList:
		
		#upcPhoto = barcodeFormat(item, writer=ImageWriter())
		upcPhoto = EAN13(item, writer=ImageWriter())
		
		pathToUpcPhoto = os.path.join(path, item, str(item)+suf)
		
		upcPhoto.save(pathToUpcPhoto)


def barcodeSheetCreator(upcList, dfDict, priceDict, valueDict, qtyDict):

		f = open(st.pathToCssData, 'r')
		cssData = f.read()
		f.close()
		
		f = open(st.pathToJsForBcSheet, 'r')
		js = f.read()
		f.close()
		
		f = open(st.pathToJsForSearchBar, 'r')
		jsForSb = f.read()
		f.close()

		fout = open(st.pathToBarcodeSheet, "w")
		
		fout.write(cssData)
		fout.write("\n<body>\n<div class=\"outer-grid\">\n<div class=\"inner-grid\">\n")
		#fout.write("\n<>")
		fout.write(jsForSb)
		

		
		for item in upcList:

			fout.write(f"<div id={item}>\n\t<button type=\"button\" class=\"collapsible\"> {dfDict.get(item)}({item})</button>\n\t<div class=\"content\">")
			
			fout.write(f"\n\t\t<p><h3>{dfDict.get(item)}</h3>\n\t\t<h3>{priceDict.get(item)}\n\t\t<h3>Value: {valueDict.get(item)}</h3>\n\t\t<h3>QTY: {qtyDict.get(item)}</h3>\n\t\t<h4><a href=https://data.sojournerlogistics.com/siteData/products/"+str(item)+"_page.html>"+str(item) + " Photo Link" + "</a>"+"</h4>")
			
			fout.write(f"\n\t\t<img src=\"../images/{item}/{item}_barcode.png\" width=\"225\" height=\"150\"\n") 
 
			fout.write("\t\tonerror=\"this.style.display='none'\"</p>\n\n")
			
			fout.write("\n</div>\n\n")

		fout.write(js)	
		fout.write("\n</div>\n</div>\n</body>\n</html>")

		fout.close()

def barcodesHandler(upcList, ctData, checkForPhotosArray):
		barcodeCreator(checkForPhotosArray[0], st.barcodePhotoSuf, st.pathToUpcImagesDir)
		barcodeSheetCreator(upcList, ctData[0], ctData[1], ctData[3], ctData[2])

# upcBarcodeCreator(ct.upcList, ct.dfDict, ct.priceDict, ct.valueDict, ct.qtyDict)







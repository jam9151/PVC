#written by Jesse McNary
import settings as st
import os
import check_toolV1 as ct

from datetime import datetime
def upcBarcodeCreator(upcList, dfDict, priceDict, valueDict, qtyDict):

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

			#fout.write(f"<div id={item}>\n\t\t{dict.get(item)}\n")
			
			#fout.write(f" <div id={item}>\n<left>{dict.get(item)}</left>")
			fout.write(f"<div id={item}>\n\t<button type=\"button\" class=\"collapsible\"> {dfDict.get(item)}({item})</button>\n\t<div class=\"content\">")
			fout.write(f"\n\t\t<p><h3>{dfDict.get(item)}</h3>\n\t\t<h3>{priceDict.get(item)}\n\t\t<h3>Value: {valueDict.get(item)}</h3>\n\t\t<h3>QTY: {qtyDict.get(item)}</h3>")
			fout.write(f"\n\t\t<img src=\"../images/{item}/{item}_barcode.png\" width=\"225\" height=\"150\"\n") 
			fout.write("\t\tonerror=\"this.style.display='none'\"</p>\n\n")
			fout.write("\n</div>\n\n")
			'''
			if(i == (len(upcList) // 3)):
				fout.write("</div>\n<div class=\"inner-grid\">\n\n")
			elif(i == (len(upcList) // 3) * 2 ):
				fout.write("</div>\n<div class=\"inner-grid\">\n\n")
			#elif(i == (len(upcList) // 4) * 3 ):
				#fout.write("</div>\n<div class=\"inner-grid\">\n\n")
			
			i+=1
			'''

		fout.write(js)	
		fout.write("\n</div>\n</div>\n</body>\n</html>")

		fout.close()

upcBarcodeCreator(ct.upcList, ct.dfDict, ct.priceDict, ct.valueDict, ct.qtyDict)







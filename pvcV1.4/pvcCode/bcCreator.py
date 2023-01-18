#written by Jesse McNary
import os, sys
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

		

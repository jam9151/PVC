import check_toolV1 as ct
import settings as st
import os
import shutil

def sortFiles(path,upcList,suf, ext):
	
	shutiledItems = []
	
	for item in upcList:
		print(upcList)
		newPathToImagesDir = os.path.join(st.pathToUpcImagesDir, str(item))
	
		pathToPhoto = os.path.join(path, str(item)+suf+ext)

		finalDes = os.path.join(newPathToImagesDir, str(item)+suf+ext)

		isFile = os.path.exists(finalDes)

		if isFile == False:
			shutil.copy(pathToPhoto, newPathToImagesDir)
			
			doubleCheck = os.path.exists(finalDes)

			if doubleCheck == True:
				os.remove(pathToPhoto)
				shutiledItems.append(str(item)+suf+ext)

			else:
				print("Error, File did not transfer.")

		else:
			print("File Exists"+str(item))
	return shutiledItems
	

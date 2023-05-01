import checkTool as ct
import settings as st
import os
import shutil

def sortFiles(path,upcList,suf, ext):
	
	shutiledItems = []
	
	for item in upcList:
		
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

def sortFilesToDir(result):
		with open(st.pathToShutilLogsTextFile, "a") as f:
			frontSent = sortFiles(st.pathToNas, result[2], st.frontOfBox, st.jpg)
			print("_front sent", frontSent, "\n", file=f)
			
			sideSent = sortFiles(st.pathToNas, result[3], st.sideOfBox, st.jpg)
			print("_side sent", sideSent, "\n", file=f)

			backSent = sortFiles(st.pathToNas, result[4], st.backOfBox, st.jpg)
			print("_back sent", backSent, "\n", file=f)

			angleSent = sortFiles(st.pathToNas, result[5], st.angleOfBox, st.jpg)
			print("_angle sent", angleSent, "\n", file=f)
		f.close()
	

Product View Compendium(10/28/2022)
Created by Jesse McNary and Joel Duggins. With help from Christopher Moore.

	The Product View Compendium or PVC for short is a tool to aid purchasers during item pursuit. The idea behind the  
project was to create a system that allowed purchasers to be able to show venue employees important item information to help find items faster and with ease.
This information includes photos of the front, back, side, an angled photo showing both the side and front together, barcode photo, UPC number, item price and description.

How the program functions.
1) runSystem.sh is run on the virtual machine hidden12 bihourly / hourly.
	-removes the old purchasing sheet then download the most up to date version.
	-runs script main.py
	-sftp the siteData directory to the SL data site.(in progress)
2) main.py
	-main is the script that runs the data check and creation tools.
	2a) main.py is run, this calls the function checkForPhotos() where check_toolV1.checktool() is called 5 times, each call checks for
		items named (UPC)(_suf).(ext); For example 01109412321_front.jpg would be the front of the box, the webpage would be named 01109412321_page.html.
		checkForPhotos() generates 5 different lists full of upc numbers that do not have corisponding files inside of pvc/siteData/images and pvc/siteData/products.
	
	2b) The next function called inside of main is checkForDirAndMake(). This function calles 2 separate functions pageCreator.upcDirCheck() and pageCreator.upcHtmlCreator()| upcDirCheck() does as it says, 
		it goes checks if a directory named (upc) exists, if it does not exist the function creates a new one. upcHtmlCreator has the same functionality as upcDirCheck() except it creates html pages based on template.html.
	
	2c) the final function called is barcodesHandler() this function calls barcodeCreator.barcodeCreator() which takes the list generated from checkForPhotos() and creates a barcode for every new item added to
		the purchasing sheet. 

	If there are any other questions about how the code after reading part 2, feel free to consult me (Jesse McNary) and I would be happy to sit down and have a conversation.
3) Important Q/A
	a) Q: Where does the system get the original list of UPCs which the program checks for?
	   A: The original list of UPCs is generated in the check_toolV1.py module. When runSystem.sh is run the old purchasing sheet is deleted and a new one is downloaded, 
		this keeps the original upc list as up to date as possible.
	
	b) Q: Will the PVC system encounter an error if columns are moved around in the purchasing sheet?
	   A: The system currently filters the purchasing sheet into a pandas data frame, It is then filtered down into a smaller dataframe with only column C(Item Description), F(Price), H(y/n), and K(UPC number). 
		IF AT ANY POINT THESE COLUMN ORDERS CHANGE, the system will not work as intended.
	
	c) Q: Where is the system running?
	   A: As of 10/28/2022 the system is running off a virtual machine on hidden0 named hidden12.
	
	d) Q: How do the purchasers access the webpages created by the PVC system?
	   A: All webpages will be sent directly to the sojourner data site, purchasers need to direct themselves to the purchasing sheet where they will be able to click on imbedded links in the UPC Column.

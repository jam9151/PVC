Step1: Download recent SVRC or Lapis inventory report
Step2: Copy data (WITHOUT FORMATTING, CTRL + SHIFT + V) from each column and paste in the correct order. A = QTY, B = UPC, C = Brand, D = Model, E = ItemDescription, F = Condition. 
Step3: open listOfPhotosNeeded.xlsx and copy column
=EQ(VLOOKUP(H:H, B:B, 1, FALSE), H:H)
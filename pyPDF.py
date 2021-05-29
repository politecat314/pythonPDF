from PIL import Image
from PyPDF2 import PdfFileMerger
import os

# add all images and pdfs to this list. Processed stuff goes into mergeList
rawList = ['hello.pdf', 'myImages.pdf','Img1.jpg','Img2.jpg']
print("Raw files: " + str(rawList))

# merge everything inside this list
mergeList = []
temp = []

tempCounter = 0 # for naming the temporary files

for file in rawList:
    if file.split(".")[1] == 'pdf':
        mergeList.append(file)
    else:
        image = Image.open(file)
        im = image.convert('RGB')
        filename = "_temp_" + str(tempCounter) + ".pdf"
        im.save(filename)
        mergeList.append(filename)
        temp.append(filename)
        tempCounter += 1
        
        
print("Processed files: " + str(mergeList))
print("Temporary files generated: " + str(temp))


merger = PdfFileMerger()

for pdf in mergeList:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
print("Merged PDF generated")

# delete the temporary files
for file in temp:
    os.remove(file)
    
print("Temporary files removed")